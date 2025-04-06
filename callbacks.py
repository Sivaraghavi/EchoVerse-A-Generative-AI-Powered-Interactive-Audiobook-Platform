from dash import Input, Output, State, callback, exceptions, html, dcc, callback_context

import plotly.graph_objs as go
import base64, os, pdfplumber
from datetime import datetime

from ai import generate_response, generate_fanfiction, get_voice_input, speak
from database import (
    get_interactions, save_interaction, save_fanfiction,
    get_public_fanfictions, update_streaks, get_streaks, get_activity
)
from components import home_page, book_details_page, fanfiction_page, dashboard_page

# Global book library and chapters
book_library = [
    {
        "id": "harry-potter",
        "title": "Harry Potter and the Sorcerer's Stone",
        "cover": "harry_potter.jpg",
        "summary": "A young wizard discovers his magical heritage and attends Hogwarts."
    },
    {
        "id": "percy-jackson",
        "title": "Percy Jackson & The Lightning Thief",
        "cover": "percy_jackson.jpg",
        "summary": "A teenager learns he is the son of a Greek god and battles monsters."
    },
    {
        "id": "lotr-fellowship",
        "title": "The Lord of the Rings: The Fellowship of the Ring",
        "cover": "lotr_fellowship.jpg",
        "summary": "A hobbit embarks on a perilous journey to destroy a powerful ring."
    }
]

book_chapters = {
    "harry-potter": {
        0: "Chapter 1: Harry lives under the stairs at Privet Drive...",
        1: "Chapter 2: A letter from Hogwarts changes his life..."
    },
    "percy-jackson": {
        0: "Chapter 1: Percy faces a monstrous challenge on a school trip...",
        1: "Chapter 2: He learns about his divine heritage at Camp Half-Blood..."
    },
    "lotr-fellowship": {
        0: "Chapter 1: Frodo inherits a mysterious ring from Bilbo...",
        1: "Chapter 2: The journey begins as the fellowship is formed..."
    }
}

# -------------------------------
# Utility: Process PDF file
# -------------------------------
def process_pdf(file_path):
    chapters = {}
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages[:2]):
            text = page.extract_text() or f"Chapter {i+1}: [Text unavailable]"
            chapters[i] = text[:200]
    return chapters

# -------------------------------
# Page Routing Callback
# -------------------------------
@callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/':
        return home_page()
    elif pathname.startswith('/book/'):
        book_id = pathname.split('/book/')[1]
        return book_details_page(book_id)
    elif pathname == '/fanfiction':
        return fanfiction_page()
    elif pathname == '/dashboard':
        return dashboard_page()
    return home_page()

# -------------------------------
# Sidebar Toggle Callback
# -------------------------------

@callback(
    Output('sidebar', 'className'),
    [Input('hamburger-btn', 'n_clicks'),
     Input('page-content', 'n_clicks')],
    State('sidebar', 'className'),
    prevent_initial_call=True
)
def toggle_sidebar(hamburger_clicks, content_clicks, current_class):
    ctx = callback_context  # use the imported callback_context directly
    if not ctx.triggered:
        raise exceptions.PreventUpdate
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if trigger_id == 'hamburger-btn':
        return 'sidebar' if 'hidden' in current_class else 'sidebar hidden'
    if trigger_id == 'page-content' and 'hidden' not in current_class:
        return 'sidebar hidden'
    raise exceptions.PreventUpdate

# -------------------------------
# Book Grid Update (Search & PDF Upload)
# -------------------------------
@callback(
    Output('book-grid', 'children'),
    [Input('search-input', 'value'),
     Input('upload-pdf', 'contents')],
    [State('upload-pdf', 'filename'),
     State('search-input', 'value')],
    prevent_initial_call=True
)
def update_book_grid(search_value, upload_contents, filename, current_search):
    # First, if a PDF is uploaded, process it
    if upload_contents and filename:
        with open("temp.pdf", "wb") as f:
            f.write(base64.b64decode(upload_contents.split(',')[1]))
        chapters = process_pdf("temp.pdf")
        os.remove("temp.pdf")
        book_id = filename.split('.')[0].lower().replace(" ", "-")
        new_book = {
            "id": book_id,
            "title": filename,
            "cover": "upload_pdf.jpg",
            "summary": "User uploaded PDF book."
        }
        book_library.append(new_book)
        book_chapters[book_id] = chapters
        # Reset upload_contents to avoid reprocessing
        upload_contents = None

    # Now, filter the book library based on the search value.
    if not search_value:
        filtered_books = book_library
    else:
        search_lower = search_value.lower()
        filtered_books = [b for b in book_library if search_lower in b["title"].lower()]
    
    cards = []
    for book in filtered_books:
        cards.append(
            html.Div(className='book-card', children=[
                html.Img(src=f'/assets/{book["cover"]}', className='book-cover'),
                html.P(book["title"], className='book-title'),
                html.P(book["summary"], className='book-summary'),
                dcc.Link("Select", href=f'/book/{book["id"]}', className='select-btn')
            ])
        )
    # Always add the upload PDF card (if not already added in header)
    cards.append(
        html.Div(className='book-card', children=[
            html.Img(src='/assets/upload_pdf.jpg', className='book-cover'),
            html.P("Upload Your Own PDF"),
            dcc.Upload(id='upload-pdf', children=html.Button('Upload', className='upload-btn'))
        ])
    )
    return cards

# -------------------------------
# Book Details: Chapter Dropdown Callback
# -------------------------------
@callback(
    [Output('chapter-select', 'options'),
     Output('chapter-text', 'children')],
    [Input('url', 'pathname'),
     Input('chapter-select', 'value')],
    prevent_initial_call=True
)
def update_chapter_content(pathname, chapter_idx):
    if not pathname.startswith('/book/'):
        raise exceptions.PreventUpdate
    book_id = pathname.split('/book/')[1]
    if book_id not in book_chapters:
        return [], "No chapters available."
    options = [{'label': f"Chapter {i+1}", 'value': i} for i in book_chapters[book_id].keys()]
    text = book_chapters[book_id].get(chapter_idx, "Select a chapter")
    return options, text

# -------------------------------
# Narrate Button Callback
# -------------------------------
@callback(
    Output('chapter-text', 'children', allow_duplicate=True),
    Input('narrate-btn', 'n_clicks'),
    State('chapter-text', 'children'),
    prevent_initial_call=True
)
def narrate_chapter(n_clicks, text):
    if n_clicks and "Select a chapter" not in text:
        speak(text)
    return text

# -------------------------------
# Chat Update Callback
# -------------------------------
@callback(
    Output('chat-history', 'children'),
    [Input('send-btn', 'n_clicks'),
     Input('speak-btn', 'n_clicks')],
    [State('chat-input', 'value'),
     State('chapter-text', 'children'),
     State('url', 'pathname')]
)
def update_chat(send_clicks, speak_clicks, user_input, chapter_text, pathname):
    user_id = "user1"
    if not pathname.startswith('/book/') or not chapter_text or "Select" in chapter_text:
        return "Select a book and chapter first"
    book_id = pathname.split('/book/')[1]
    past = get_interactions(user_id, book_id)
    ctx = dash.callback_context
    if not ctx.triggered or (send_clicks == 0 and speak_clicks == 0):
        return html.Ul([html.Li(p) for p in past]) if past else "Start chatting!"
    if speak_clicks:
        user_input = get_voice_input()
    if user_input and "Error" not in user_input and "Timeout" not in user_input:
        response = generate_response(user_input, chapter_text, past)
        save_interaction(user_id, book_id, chapter_text[:50], user_input, response)
        past.append(f"You: {user_input} | AI: {response}")
    return html.Ul([html.Li(p) for p in past])

# -------------------------------
# Fanfiction Generation Callback
# -------------------------------
@callback(
    Output('fanfic-output', 'children'),
    Input('generate-fanfic-btn', 'n_clicks'),
    [State('fanfic-prompt', 'value'),
     State('visibility', 'value'),
     State('url', 'pathname')],
    prevent_initial_call=True
)
def generate_fanfic(n_clicks, prompt, visibility, pathname):
    user_id = "user1"
    if not n_clicks or not prompt or not pathname.startswith('/book/'):
        raise exceptions.PreventUpdate
    book_id = pathname.split('/book/')[1]
    chapters = book_chapters.get(book_id, {})
    fanfic = generate_fanfiction(book_id, chapters, prompt)
    fanfic_text = "\n\n".join([f"Chapter {i+1}: {chapter}" for i, chapter in enumerate(fanfic)])
    save_fanfiction(user_id, book_id, prompt, fanfic_text, visibility)
    return html.Pre(fanfic_text)

# -------------------------------
# Fanfiction Library Callback
# -------------------------------
@callback(
    Output('fanfic-library', 'children'),
    Input('generate-fanfic-btn', 'n_clicks'),
    prevent_initial_call=True
)
def update_library(n_clicks):
    fanfics = get_public_fanfictions()
    return html.Ul([
        html.Li(f"{f['book']} - {f['prompt']}: {f['text'][:100]}...")
        for f in fanfics
    ])

# -------------------------------
# Dashboard Callback
# -------------------------------
@callback(
    [Output('streak-calendar', 'children'),
     Output('activity-graph', 'figure'),
     Output('recommendations', 'children')],
    Input('url', 'pathname')
)
def update_dashboard(pathname):
    user_id = "user1"
    if pathname != '/dashboard':
        raise exceptions.PreventUpdate
    update_streaks(user_id)
    streak = get_streaks(user_id)
    activity = get_activity(user_id)
    calendar = html.Div([
        html.Span(f"Day {i+1}: {'✅' if i < streak else '❌'} ", style={'margin': '0 5px'})
        for i in range(7)
    ], style={'text-align': 'center'})
    fig = go.Figure(
        data=[go.Bar(
            x=list(activity.keys()),
            y=list(activity.values()),
            marker_color='#FF0000'
        )],
        layout=go.Layout(
            plot_bgcolor='#333333',
            paper_bgcolor='#333333',
            font=dict(color='#FFFFFF')
        )
    )
    recs = "Try 'The Hobbit' for more fantasy adventures!"
    return calendar, fig, recs

