# # # from dash import dcc, html
# # # import dash_bootstrap_components as dbc

# # # def layout():
# # #     return html.Div([
# # #         dcc.Location(id='url', refresh=False),
# # #         html.Div(id='page-content'),
        
# # #         # Hidden div to store temporary data
# # #         dcc.Store(id='session-data', storage_type='session'),
        
# # #         # Global loading spinner
# # #         dcc.Loading(
# # #             id="loading-global",
# # #             type="circle",
# # #             children=html.Div(id="loading-output")
# # #         )
# # #     ], className='app-container')

# # # def home_page():
# # #     return html.Div([
# # #         html.Header(className='app-header', children=[
# # #             html.H1("EchoVerse", className='app-title'),
# # #             html.Div(className='app-subtitle', children="AI-Powered Interactive Audiobooks")
# # #         ]),
        
# # #         dbc.Container([
# # #             dbc.Row([
# # #                 dbc.Col([
# # #                     dcc.Input(
# # #                         id='search-books',
# # #                         type='text',
# # #                         placeholder='🔍 Search for books...',
# # #                         className='search-input'
# # #                     )
# # #                 ], width=12)
# # #             ]),
            
# # #             html.H2("Featured Books", className='section-title'),
            
# # #             dbc.Row([
# # #                 dbc.Col([
# # #                     dbc.Card([
# # #                         dbc.CardImg(
# # #                             src="/assets/harry_potter_and_the_sorcerers_stone.jpg",
# # #                             top=True,
# # #                             className='book-cover'
# # #                         ),
# # #                         dbc.CardBody([
# # #                             html.H4("Harry Potter and the Sorcerer's Stone", className='book-title'),
# # #                             dbc.Button(
# # #                                 "Explore",
# # #                                 id='hp-button',
# # #                                 href="/book/Harry%20Potter%20and%20the%20Sorcerer%E2%80%99s%20Stone",
# # #                                 className='explore-button'
# # #                             )
# # #                         ])
# # #                     ], className='book-card')
# # #                 ], md=4),
                
# # #                 dbc.Col([
# # #                     dbc.Card([
# # #                         dbc.CardImg(
# # #                             src="/assets/percy_jackson_&_the_lightning_thief.jpg",
# # #                             top=True,
# # #                             className='book-cover'
# # #                         ),
# # #                         dbc.CardBody([
# # #                             html.H4("Percy Jackson & The Lightning Thief", className='book-title'),
# # #                             dbc.Button(
# # #                                 "Explore",
# # #                                 id='pj-button',
# # #                                 href="/book/Percy%20Jackson%20%26%20The%20Lightning%20Thief",
# # #                                 className='explore-button'
# # #                             )
# # #                         ])
# # #                     ], className='book-card')
# # #                 ], md=4),
                
# # #                 dbc.Col([
# # #                     dbc.Card([
# # #                         dbc.CardImg(
# # #                             src="/assets/logo.png",  # Placeholder for additional books
# # #                             top=True,
# # #                             className='book-cover'
# # #                         ),
# # #                         dbc.CardBody([
# # #                             html.H4("Upload Your Own Book", className='book-title'),
# # #                             dcc.Upload(
# # #                                 id='upload-book',
# # #                                 children=dbc.Button(
# # #                                     "Upload PDF",
# # #                                     className='upload-button'
# # #                                 ),
# # #                                 multiple=False
# # #                             )
# # #                         ])
# # #                     ], className='book-card')
# # #                 ], md=4)
# # #             ])
# # #         ], className='main-container'),
        
# # #         footer()
# # #     ])

# # # def book_details_page(book_name):
# # #     return html.Div([
# # #         html.Header(className='app-header', children=[
# # #             html.H1("EchoVerse", className='app-title'),
# # #             html.Div(className='app-subtitle', children=f"Exploring: {book_name}")
# # #         ]),
        
# # #         dbc.Container([
# # #             dbc.Row([
# # #                 dbc.Col([
# # #                     html.Img(
# # #                         src=f"/assets/{book_name.replace(' ', '_').lower()}.jpg",
# # #                         className='book-detail-cover'
# # #                     )
# # #                 ], md=4),
                
# # #                 dbc.Col([
# # #                     html.H2(book_name, className='book-detail-title'),
# # #                     html.Div(className='book-meta', children=[
# # #                         html.Span("Fantasy", className='genre-tag'),
# # #                         html.Span("300 pages", className='page-count')
# # #                     ]),
                    
# # #                     dcc.Dropdown(
# # #                         id='chapter-selector',
# # #                         options=[
# # #                             {'label': 'Chapter 1', 'value': 0},
# # #                             {'label': 'Chapter 2', 'value': 1}
# # #                         ],
# # #                         placeholder="Select a chapter...",
# # #                         className='chapter-dropdown'
# # #                     ),
                    
# # #                     html.Div(id='chapter-content', className='chapter-content'),
                    
# # #                     dbc.ButtonGroup([
# # #                         dbc.Button(
# # #                             "🎧 Narrate Chapter",
# # #                             id='narrate-button',
# # #                             className='action-button'
# # #                         ),
# # #                         dbc.Button(
# # #                             "📖 Read Aloud",
# # #                             id='read-button',
# # #                             className='action-button'
# # #                         )
# # #                     ], className='action-button-group')
# # #                 ], md=8)
# # #             ]),
            
# # #             html.Hr(),
            
# # #             html.H3("Discuss with AI Buddy", className='section-title'),
            
# # #             dbc.Row([
# # #                 dbc.Col([
# # #                     dcc.Textarea(
# # #                         id='chat-input',
# # #                         placeholder='Ask about this chapter or book...',
# # #                         className='chat-input'
# # #                     ),
                    
# # #                     dbc.ButtonGroup([
# # #                         dbc.Button(
# # #                             "🎤 Speak",
# # #                             id='voice-input-button',
# # #                             className='voice-button'
# # #                         ),
# # #                         dbc.Button(
# # #                             "✉️ Send",
# # #                             id='send-message-button',
# # #                             className='send-button'
# # #                         )
# # #                     ], className='chat-button-group')
# # #                 ], md=8),
                
# # #                 dbc.Col([
# # #                     html.Div(id='chat-history', className='chat-history')
# # #                 ], md=4)
# # #             ]),
            
# # #             html.Hr(),
            
# # #             html.H3("Create Fanfiction", className='section-title'),
            
# # #             dbc.Row([
# # #                 dbc.Col([
# # #                     dcc.Textarea(
# # #                         id='fanfiction-prompt',
# # #                         placeholder='What if... (describe your alternate story idea)',
# # #                         className='fanfiction-input'
# # #                     ),
                    
# # #                     dbc.RadioItems(
# # #                         id='fanfiction-visibility',
# # #                         options=[
# # #                             {'label': 'Public', 'value': 'public'},
# # #                             {'label': 'Private', 'value': 'private'}
# # #                         ],
# # #                         value='public',
# # #                         inline=True,
# # #                         className='visibility-options'
# # #                     ),
                    
# # #                     dbc.Button(
# # #                         "✨ Generate Fanfiction",
# # #                         id='generate-fanfiction-button',
# # #                         className='generate-button'
# # #                     )
# # #                 ], md=8),
                
# # #                 dbc.Col([
# # #                     html.Div(id='fanfiction-output', className='fanfiction-output')
# # #                 ], md=4)
# # #             ])
# # #         ], className='main-container'),
        
# # #         footer()
# # #     ])

# # # def fanfiction_page():
# # #     return html.Div([
# # #         html.Header(className='app-header', children=[
# # #             html.H1("EchoVerse", className='app-title'),
# # #             html.Div(className='app-subtitle', children="Fanfiction Library")
# # #         ]),
        
# # #         dbc.Container([
# # #             dbc.Row([
# # #                 dbc.Col([
# # #                     html.H2("Community Creations", className='section-title'),
# # #                     html.Div(id='fanfiction-library', className='fanfiction-library')
# # #                 ], md=8),
                
# # #                 dbc.Col([
# # #                     html.H2("Your Fanfictions", className='section-title'),
# # #                     html.Div(id='user-fanfictions', className='user-fanfictions')
# # #                 ], md=4)
# # #             ])
# # #         ], className='main-container'),
        
# # #         footer()
# # #     ])

# # # def dashboard_page():
# # #     return html.Div([
# # #         html.Header(className='app-header', children=[
# # #             html.H1("EchoVerse", className='app-title'),
# # #             html.Div(className='app-subtitle', children="Your Reading Dashboard")
# # #         ]),
        
# # #         dbc.Container([
# # #             dbc.Row([
# # #                 dbc.Col([
# # #                     html.H2("Reading Streak", className='section-title'),
# # #                     html.Div(id='streak-calendar', className='streak-calendar')
# # #                 ], md=4),
                
# # #                 dbc.Col([
# # #                     html.H2("Your Activity", className='section-title'),
# # #                     dcc.Graph(id='activity-graph', className='activity-graph')
# # #                 ], md=8)
# # #             ]),
            
# # #             dbc.Row([
# # #                 dbc.Col([
# # #                     html.H2("Recommended Books", className='section-title'),
# # #                     html.Div(id='book-recommendations', className='book-recommendations')
# # #                 ], md=12)
# # #             ])
# # #         ], className='main-container'),
        
# # #         footer()
# # #     ])

# # # def footer():
# # #     return html.Footer(className='app-footer', children=[
# # #         dbc.Container([
# # #             dbc.Row([
# # #                 dbc.Col([
# # #                     html.H4("Connect With Us", className='footer-title'),
# # #                     html.Div(className='social-links', children=[
# # #                         html.A(
# # #                             html.Img(src="/assets/githubicon.png", className='social-icon'),
# # #                             href="https://github.com/yourusername",
# # #                             target="_blank"
# # #                         ),
# # #                         html.A(
# # #                             html.Img(src="/assets/linkedinicon.png", className='social-icon'),
# # #                             href="https://linkedin.com/in/yourprofile",
# # #                             target="_blank"
# # #                         ),
# # #                         html.A(
# # #                             html.Img(src="/assets/twittericon.png", className='social-icon'),
# # #                             href="https://twitter.com/yourhandle",
# # #                             target="_blank"
# # #                         ),
# # #                         html.A(
# # #                             html.Img(src="/assets/mailicon.png", className='social-icon'),
# # #                             href="mailto:youremail@example.com"
# # #                         )
# # #                     ])
# # #                 ], md=4),
                
# # #                 dbc.Col([
# # #                     html.H4("About EchoVerse", className='footer-title'),
# # #                     html.P("An AI-powered interactive audiobook platform that brings stories to life with generative AI and voice technology.", className='footer-description')
# # #                 ], md=4),
                
# # #                 dbc.Col([
# # #                     html.H4("Developer", className='footer-title'),
# # #                     html.Div(className='developer-info', children=[
# # #                         html.Img(
# # #                             src="/assets/developerface.jpg",
# # #                             className='developer-image'
# # #                         ),
# # #                         html.Div([
# # #                             html.P("Created by Your Name", className='developer-name'),
# # #                             html.P("AI & Voice Technology Enthusiast", className='developer-title')
# # #                         ])
# # #                     ])
# # #                 ], md=4)
# # #             ]),
            
# # #             html.Hr(className='footer-divider'),
            
# # #             html.P("© 2025 EchoVerse. All rights reserved.", className='copyright')
# # #         ])
# # #     ])

# # from dash.dependencies import Input, Output, State
# # from app import app
# # from components.pages import home_page, book_details_page, fanfiction_page, dashboard_page
# # from ai import generate_response, get_voice_input, speak, generate_fanfiction
# # from database import get_interactions, save_interaction, save_fanfiction, get_public_fanfictions, update_reading_streak, get_reading_streak
# # import plotly.graph_objs as go
# # from dash import html

# # # Page routing
# # @app.callback(
# #     Output('page-content', 'children'),
# #     Input('url', 'pathname')
# # )
# # def display_page(pathname):
# #     if pathname == '/':
# #         return home_page()
# #     elif pathname.startswith('/book/'):
# #         book_name = pathname.split('/book/')[-1].replace('%20', ' ')
# #         return book_details_page(book_name)
# #     elif pathname == '/fanfiction':
# #         return fanfiction_page()
# #     elif pathname == '/dashboard':
# #         return dashboard_page()
# #     return html.H1('404 - Page Not Found')

# # # Sidebar toggle
# # @app.callback(
# #     Output('sidebar', 'className'),
# #     Input('hamburger-btn', 'n_clicks'),
# #     State('sidebar', 'className')
# # )
# # def toggle_sidebar(n_clicks, current_class):
# #     if n_clicks:
# #         return 'sideBar' if 'hidden' in current_class else 'sideBar hidden'
# #     return current_class

# # # Chapter text update
# # @app.callback(
# #     Output('chapter-text', 'children'),
# #     Input('chapter-dropdown', 'value'),
# #     State('url', 'pathname')
# # )
# # def update_chapter_text(chapter, pathname):
# #     book_name = pathname.split('/book/')[-1].replace('%20', ' ')
# #     return f"Sample text for {book_name}, Chapter {chapter}"

# # # Narration
# # @app.callback(
# #     Output('loading-output', 'children'),
# #     Input('narrate-btn', 'n_clicks'),
# #     State('chapter-text', 'children')
# # )
# # def narrate_chapter(n_clicks, chapter_text):
# #     if n_clicks:
# #         speak(chapter_text)
# #         return "Narrated successfully"
# #     return ""

# # # Chat with AI
# # @app.callback(
# #     Output('chat-history', 'children'),
# #     Input('send-btn', 'n_clicks'),
# #     State('chat-input', 'value'),
# #     State('chapter-text', 'children'),
# #     State('chat-history', 'children'),
# #     State('url', 'pathname')
# # )
# # def update_chat(n_clicks, user_input, chapter_text, current_history, pathname):
# #     if n_clicks and user_input:
# #         book_name = pathname.split('/book/')[-1].replace('%20', ' ')
# #         user_id = "user1"  # Placeholder; replace with actual user ID logic
# #         past_interactions = get_interactions(user_id, book_name)
# #         response = generate_response(user_input, chapter_text, past_interactions)
# #         save_interaction(user_id, book_name, "Chapter 1", user_input, response)
# #         current_history = current_history or []
# #         return current_history + [html.P(f"You: {user_input}"), html.P(f"AI: {response}")]
# #     return current_history

# # # Voice input
# # @app.callback(
# #     Output('chat-input', 'value'),
# #     Input('speak-btn', 'n_clicks')
# # )
# # def handle_voice_input(n_clicks):
# #     if n_clicks:
# #         return get_voice_input()
# #     return ""

# # # Fanfiction generation
# # @app.callback(
# #     Output('fanfic-output', 'children'),
# #     Input('generate-btn', 'n_clicks'),
# #     State('fanfic-prompt', 'value'),
# #     State('fanfic-visibility', 'value'),
# #     State('url', 'pathname')
# # )
# # def generate_fanfic(n_clicks, prompt, visibility, pathname):
# #     if n_clicks and prompt:
# #         book_name = pathname.split('/book/')[-1].replace('%20', ' ')
# #         chapters = {"Chapter 1": "Sample chapter text"}  # Placeholder; expand as needed
# #         fanfic = generate_fanfiction(book_name, chapters, prompt)
# #         user_id = "user1"  # Placeholder
# #         is_public = visibility == 'public'
# #         save_fanfiction(user_id, book_name, prompt, "\n".join(fanfic), is_public)
# #         return html.Div([html.P(chap) for chap in fanfic])
# #     return ""

# # # Fanfiction library
# # @app.callback(
# #     Output('fanfic-library', 'children'),
# #     Input('url', 'pathname')
# # )
# # def update_fanfic_library(pathname):
# #     if pathname == '/fanfiction':
# #         fanfics = get_public_fanfictions()
# #         return [html.Div([html.H3(f["book"]), html.P(f["text"])]) for f in fanfics]
# #     return ""

# # # Dashboard updates
# # @app.callback(
# #     [Output('streak-calendar', 'children'),
# #      Output('activity-graph', 'figure'),
# #      Output('recommendations', 'children')],
# #     Input('url', 'pathname')
# # )
# # def update_dashboard(pathname):
# #     if pathname == '/dashboard':
# #         user_id = "user1"  # Placeholder
# #         update_reading_streak(user_id)
# #         streak = get_reading_streak(user_id)
# #         streak_text = f"Current: {streak['current']} days | Longest: {streak['longest']} days"
        
# #         figure = {
# #             'data': [go.Bar(x=['Books Read', 'Fanfics'], y=[2, 1])],
# #             'layout': {'title': 'Activity', 'paper_bgcolor': '#2c3e50', 'plot_bgcolor': '#34495e'}
# #         }
        
# #         recs = html.P("Try 'Sample Book 3'")
# #         return streak_text, figure, recs
# #     return "", {}, ""


# from dash import Input, Output, State, callback, exceptions, html, dcc, callback_context
# import dash

# import plotly.graph_objs as go
# import base64, os, pdfplumber
# from datetime import datetime

# from ai import generate_response, generate_fanfiction, get_voice_input, speak
# from database import (
#     get_interactions, save_interaction, save_fanfiction,
#     get_public_fanfictions, update_streaks, get_streaks, get_activity
# )
# from components import home_page, book_details_page, fanfiction_page, dashboard_page

# # Global book library and chapters
# book_library = [
#     {
#         "id": "harry-potter",
#         "title": "Harry Potter and the Sorcerer's Stone",
#         "cover": "harry_potter.jpg",
#         "summary": "A young wizard discovers his magical heritage and attends Hogwarts."
#     },
#     {
#         "id": "percy-jackson",
#         "title": "Percy Jackson & The Lightning Thief",
#         "cover": "percy_jackson.jpg",
#         "summary": "A teenager learns he is the son of a Greek god and battles monsters."
#     },
#     {
#         "id": "lotr-fellowship",
#         "title": "The Lord of the Rings: The Fellowship of the Ring",
#         "cover": "lotr_fellowship.jpg",
#         "summary": "A hobbit embarks on a perilous journey to destroy a powerful ring."
#     }
# ]

# book_chapters = {
#     "harry-potter": {
#         0: "Chapter 1: Harry lives under the stairs at Privet Drive...",
#         1: "Chapter 2: A letter from Hogwarts changes his life..."
#     },
#     "percy-jackson": {
#         0: "Chapter 1: Percy faces a monstrous challenge on a school trip...",
#         1: "Chapter 2: He learns about his divine heritage at Camp Half-Blood..."
#     },
#     "lotr-fellowship": {
#         0: "Chapter 1: Frodo inherits a mysterious ring from Bilbo...",
#         1: "Chapter 2: The journey begins as the fellowship is formed..."
#     }
# }

# # -------------------------------
# # Utility: Process PDF file
# # -------------------------------
# def process_pdf(file_path):
#     chapters = {}
#     with pdfplumber.open(file_path) as pdf:
#         for i, page in enumerate(pdf.pages[:2]):
#             text = page.extract_text() or f"Chapter {i+1}: [Text unavailable]"
#             chapters[i] = text[:200]
#     return chapters

# # -------------------------------
# # Page Routing Callback
# # -------------------------------
# @callback(
#     Output('page-content', 'children'),
#     Input('url', 'pathname')
# )
# def display_page(pathname):
#     if pathname == '/':
#         return home_page()
#     elif pathname.startswith('/book/'):
#         book_id = pathname.split('/book/')[1]
#         return book_details_page(book_id)
#     elif pathname == '/fanfiction':
#         return fanfiction_page()
#     elif pathname == '/dashboard':
#         return dashboard_page()
#     return home_page()

# # -------------------------------
# # Sidebar Toggle Callback
# # -------------------------------

# @callback(
#     Output('sidebar', 'className'),
#     [Input('hamburger-btn', 'n_clicks'),
#      Input('page-content', 'n_clicks')],
#     State('sidebar', 'className'),
#     prevent_initial_call=True
# )
# def toggle_sidebar(hamburger_clicks, content_clicks, current_class):
#     ctx = callback_context  # use the imported callback_context directly
#     if not ctx.triggered:
#         raise exceptions.PreventUpdate
#     trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
#     if trigger_id == 'hamburger-btn':
#         return 'sidebar' if 'hidden' in current_class else 'sidebar hidden'
#     if trigger_id == 'page-content' and 'hidden' not in current_class:
#         return 'sidebar hidden'
#     raise exceptions.PreventUpdate

# # -------------------------------
# # Book Grid Update (Search & PDF Upload)
# # -------------------------------
# @callback(
#     Output('book-grid', 'children'),
#     [Input('search-input', 'value'),
#      Input('upload-pdf', 'contents')],
#     [State('upload-pdf', 'filename'),
#      State('search-input', 'value')],
#     prevent_initial_call=True
# )
# def update_book_grid(search_value, upload_contents, filename, current_search):
#     # First, if a PDF is uploaded, process it
#     if upload_contents and filename:
#         with open("temp.pdf", "wb") as f:
#             f.write(base64.b64decode(upload_contents.split(',')[1]))
#         chapters = process_pdf("temp.pdf")
#         os.remove("temp.pdf")
#         book_id = filename.split('.')[0].lower().replace(" ", "-")
#         new_book = {
#             "id": book_id,
#             "title": filename,
#             "cover": "upload_pdf.jpg",
#             "summary": "User uploaded PDF book."
#         }
#         book_library.append(new_book)
#         book_chapters[book_id] = chapters
#         # Reset upload_contents to avoid reprocessing
#         upload_contents = None

#     # Now, filter the book library based on the search value.
#     if not search_value:
#         filtered_books = book_library
#     else:
#         search_lower = search_value.lower()
#         filtered_books = [b for b in book_library if search_lower in b["title"].lower()]
    
#     cards = []
#     for book in filtered_books:
#         cards.append(
#             html.Div(className='book-card', children=[
#                 html.Img(src=f'/assets/{book["cover"]}', className='book-cover'),
#                 html.P(book["title"], className='book-title'),
#                 html.P(book["summary"], className='book-summary'),
#                 dcc.Link("Select", href=f'/book/{book["id"]}', className='select-btn')
#             ])
#         )
#     # Always add the upload PDF card (if not already added in header)
#     cards.append(
#         html.Div(className='book-card', children=[
#             html.Img(src='/assets/upload_pdf.jpg', className='book-cover'),
#             html.P("Upload Your Own PDF"),
#             dcc.Upload(id='upload-pdf', children=html.Button('Upload', className='upload-btn'))
#         ])
#     )
#     return cards

# # -------------------------------
# # Book Details: Chapter Dropdown Callback
# # -------------------------------
# @callback(
#     [Output('chapter-select', 'options'),
#      Output('chapter-text', 'children')],
#     [Input('url', 'pathname'),
#      Input('chapter-select', 'value')],
#     prevent_initial_call=True
# )
# def update_chapter_content(pathname, chapter_idx):
#     if not pathname.startswith('/book/'):
#         raise exceptions.PreventUpdate
#     book_id = pathname.split('/book/')[1]
#     if book_id not in book_chapters:
#         return [], "No chapters available."
#     options = [{'label': f"Chapter {i+1}", 'value': i} for i in book_chapters[book_id].keys()]
#     text = book_chapters[book_id].get(chapter_idx, "Select a chapter")
#     return options, text

# # -------------------------------
# # Narrate Button Callback
# # -------------------------------
# @callback(
#     Output('chapter-text', 'children', allow_duplicate=True),
#     Input('narrate-btn', 'n_clicks'),
#     State('chapter-text', 'children'),
#     prevent_initial_call=True
# )
# def narrate_chapter(n_clicks, text):
#     if n_clicks and "Select a chapter" not in text:
#         speak(text)
#     return text

# # -------------------------------
# # Chat Update Callback
# # -------------------------------
# @callback(
#     Output('chat-history', 'children'),
#     [Input('send-btn', 'n_clicks'),
#      Input('speak-btn', 'n_clicks')],
#     [State('chat-input', 'value'),
#      State('chapter-text', 'children'),
#      State('url', 'pathname')]
# )
# def update_chat(send_clicks, speak_clicks, user_input, chapter_text, pathname):
#     user_id = "user1"
#     if not pathname.startswith('/book/') or not chapter_text or "Select" in chapter_text:
#         return "Select a book and chapter first"
#     book_id = pathname.split('/book/')[1]
#     past = get_interactions(user_id, book_id)
#     ctx = dash.callback_context
#     if not ctx.triggered or (send_clicks == 0 and speak_clicks == 0):
#         return html.Ul([html.Li(p) for p in past]) if past else "Start chatting!"
#     if speak_clicks:
#         user_input = get_voice_input()
#     if user_input and "Error" not in user_input and "Timeout" not in user_input:
#         response = generate_response(user_input, chapter_text, past)
#         save_interaction(user_id, book_id, chapter_text[:50], user_input, response)
#         past.append(f"You: {user_input} | AI: {response}")
#     return html.Ul([html.Li(p) for p in past])

# # -------------------------------
# # Fanfiction Generation Callback
# # -------------------------------
# @callback(
#     Output('fanfic-output', 'children'),
#     Input('generate-fanfic-btn', 'n_clicks'),
#     [State('fanfic-prompt', 'value'),
#      State('visibility', 'value'),
#      State('url', 'pathname')],
#     prevent_initial_call=True
# )
# def generate_fanfic(n_clicks, prompt, visibility, pathname):
#     user_id = "user1"
#     if not n_clicks or not prompt or not pathname.startswith('/book/'):
#         raise exceptions.PreventUpdate
#     book_id = pathname.split('/book/')[1]
#     chapters = book_chapters.get(book_id, {})
#     fanfic = generate_fanfiction(book_id, chapters, prompt)
#     fanfic_text = "\n\n".join([f"Chapter {i+1}: {chapter}" for i, chapter in enumerate(fanfic)])
#     save_fanfiction(user_id, book_id, prompt, fanfic_text, visibility)
#     return html.Pre(fanfic_text)

# # -------------------------------
# # Fanfiction Library Callback
# # -------------------------------
# @callback(
#     Output('fanfic-library', 'children'),
#     Input('generate-fanfic-btn', 'n_clicks'),
#     prevent_initial_call=True
# )
# def update_library(n_clicks):
#     fanfics = get_public_fanfictions()
#     return html.Ul([
#         html.Li(f"{f['book']} - {f['prompt']}: {f['text'][:100]}...")
#         for f in fanfics
#     ])

# # -------------------------------
# # Dashboard Callback
# # -------------------------------
# @callback(
#     [Output('streak-calendar', 'children'),
#      Output('activity-graph', 'figure'),
#      Output('recommendations', 'children')],
#     Input('url', 'pathname')
# )
# def update_dashboard(pathname):
#     user_id = "user1"
#     if pathname != '/dashboard':
#         raise exceptions.PreventUpdate
#     update_streaks(user_id)
#     streak = get_streaks(user_id)
#     activity = get_activity(user_id)
#     calendar = html.Div([
#         html.Span(f"Day {i+1}: {'✅' if i < streak else '❌'} ", style={'margin': '0 5px'})
#         for i in range(7)
#     ], style={'text-align': 'center'})
#     fig = go.Figure(
#         data=[go.Bar(
#             x=list(activity.keys()),
#             y=list(activity.values()),
#             marker_color='#FF0000'
#         )],
#         layout=go.Layout(
#             plot_bgcolor='#333333',
#             paper_bgcolor='#333333',
#             font=dict(color='#FFFFFF')
#         )
#     )
#     recs = "Try 'The Hobbit' for more fantasy adventures!"
#     return calendar, fig, recs

from dash import Input, Output, State, callback, exceptions, html, dcc, dash
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
from dash import Input, Output, State, callback, exceptions, html, dcc, callback_context
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
