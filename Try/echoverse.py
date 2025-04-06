import dash
from dash import dcc, html, Input, Output, State
import speech_recognition as sr
import pyttsx3
from transformers import pipeline
import pdfplumber
import sqlite3
import time
import os
from datetime import datetime
import plotly.graph_objs as go

# Initialize Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Initialize text-to-speech and generative AI
engine = pyttsx3.init()
generator = pipeline('text-generation', model='distilgpt2')

# Database setup (SQLite)
conn = sqlite3.connect('echoverse.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS fanfictions
             (id INTEGER PRIMARY KEY, user_id TEXT, book TEXT, prompt TEXT, text TEXT, public INTEGER, timestamp TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS interactions
             (id INTEGER PRIMARY KEY, user_id TEXT, book TEXT, chapter TEXT, user_input TEXT, ai_response TEXT, timestamp TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS streaks
             (user_id TEXT PRIMARY KEY, days INTEGER, last_login TEXT)''')
conn.commit()

# Predefined book (Harry Potter 1)
books = {
    "Harry Potter and the Sorcerer’s Stone": {
        0: "Chapter 1: Harry lived under the stairs at Privet Drive.",
        1: "Chapter 2: A letter arrived from Hogwarts, changing everything."
    }
}

# Utility Functions
def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Text-to-speech error: {e}")

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            text = recognizer.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            return "Timeout: No speech detected."
        except sr.UnknownValueError:
            return "Error: Couldn’t understand speech."
        except Exception as e:
            return f"Error: {str(e)}"

def generate_response(user_input, chapter_text, past_interactions):
    context = f"Chapter: {chapter_text}\nPast chat: {'; '.join(past_interactions)}\nYou: {user_input}\nAI Buddy:"
    response = generator(context, max_length=100, num_return_sequences=1, temperature=0.95, truncation=True)[0]['generated_text']
    return response.split("AI Buddy:")[-1].strip()

def generate_fanfiction(book, chapters, user_prompt):
    full_story = " ".join(chapters.values())
    prompt = f"Based on '{book}', where {user_prompt}, write a 3-chapter fanfiction:"
    fanfic = generator(prompt, max_length=500, num_return_sequences=1, temperature=0.9, truncation=True)[0]['generated_text']
    return fanfic.split("Chapter ")[1:] if "Chapter " in fanfic else [fanfic] * 3

def process_pdf(file_path):
    chapters = {}
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages[:2]):  # Limit to first 2 pages for simplicity
            text = page.extract_text() or f"Chapter {i+1}: [Text unavailable]"
            chapters[i] = text[:200]  # Truncate for demo
    return chapters

# Layout
app.layout = html.Div([
    html.H1("📚 EchoVerse: Your Interactive Audiobook Adventure", style={'textAlign': 'center', 'color': '#2c3e50'}),
    dcc.Tabs(id="tabs", value='story', children=[
        dcc.Tab(label='Story', value='story'),
        dcc.Tab(label='Fanfiction', value='fanfiction'),
        dcc.Tab(label='Dashboard', value='dashboard'),
    ]),
    html.Div(id='page-content', style={'padding': '20px'})
])

# Callbacks
@app.callback(Output('page-content', 'children'), Input('tabs', 'value'))
def render_content(tab):
    user_id = "user1"  # Placeholder; replace with real user auth
    if tab == 'story':
        return html.Div([
            html.H2("Choose Your Story", style={'color': '#34495e'}),
            dcc.RadioItems(id='book-option', options=['Predefined', 'Upload PDF'], value='Predefined', style={'margin': '10px'}),
            dcc.Dropdown(id='book-select', options=[{'label': k, 'value': k} for k in books.keys()], style={'width': '50%'}),
            dcc.Upload(id='upload-pdf', children=html.Button('Upload PDF'), multiple=False),
            html.H3(id='selected-book', style={'marginTop': '20px'}),
            dcc.Dropdown(id='chapter-select', style={'width': '50%', 'marginTop': '10px'}),
            html.P(id='chapter-text', style={'fontSize': '16px', 'marginTop': '20px'}),
            html.Button("🎙️ Hear Narration", id='narrate-btn', style={'margin': '10px'}),
            html.H3("Chat with AI Buddy", style={'marginTop': '20px'}),
            html.Button("🎤 Speak", id='speak-btn', style={'marginRight': '10px'}),
            dcc.Textarea(id='chat-input', placeholder="Or type here...", style={'width': '50%', 'height': '100px'}),
            html.Button("Send", id='send-btn', style={'marginTop': '10px'}),
            html.Div(id='chat-history', style={'marginTop': '20px'})
        ])
    elif tab == 'fanfiction':
        return html.Div([
            html.H2("Create Fanfiction", style={'color': '#34495e'}),
            dcc.Textarea(id='fanfic-prompt', placeholder="E.g., 'What if Harry and Ron were dating?'", style={'width': '70%', 'height': '100px'}),
            dcc.RadioItems(id='visibility', options=['Public', 'Private'], value='Private', inline=True, style={'margin': '10px'}),
            html.Button("✨ Generate Fanfiction", id='generate-fanfic-btn', style={'margin': '10px'}),
            html.Div(id='fanfic-output', style={'whiteSpace': 'pre-wrap'}),
            html.H3("Fanfiction Library", style={'marginTop': '20px'}),
            html.Div(id='fanfic-library')
        ])
    elif tab == 'dashboard':
        return html.Div([
            html.H2("Your Dashboard", style={'color': '#34495e'}),
            html.P(id='streak-info'),
            dcc.Graph(id='activity-graph'),
            html.H3("Recommended Books", style={'marginTop': '20px'}),
            html.P(id='recommendations')
        ])

@app.callback(
    [Output('book-select', 'style'), Output('upload-pdf', 'style')],
    Input('book-option', 'value')
)
def toggle_book_option(option):
    return ({'display': 'block' if option == 'Predefined' else 'none', 'width': '50%'},
            {'display': 'block' if option == 'Upload PDF' else 'none'})

@app.callback(
    [Output('selected-book', 'children'), Output('chapter-select', 'options')],
    [Input('book-select', 'value'), Input('upload-pdf', 'filename'), Input('upload-pdf', 'contents')]
)
def update_book_selection(book, filename, contents):
    if book:
        selected_book = book
        chapters = books[book]
    elif filename and contents:
        with open("temp.pdf", "wb") as f:
            import base64
            f.write(base64.b64decode(contents.split(',')[1]))
        chapters = process_pdf("temp.pdf")
        selected_book = filename
        books[filename] = chapters
        os.remove("temp.pdf")
    else:
        return "No book selected", []
    return f"Selected: {selected_book}", [{'label': f"Chapter {i+1}", 'value': i} for i in chapters.keys()]

@app.callback(
    Output('chapter-text', 'children'),
    [Input('chapter-select', 'value'), Input('selected-book', 'children')]
)
def update_chapter_text(chapter, book_name):
    if chapter is None or not book_name:
        return "Select a chapter"
    book = book_name.split("Selected: ")[1]
    return books[book][chapter]

@app.callback(
    Output('chapter-text', 'children', allow_duplicate=True),
    Input('narrate-btn', 'n_clicks'),
    State('chapter-text', 'children'),
    prevent_initial_call=True
)
def narrate_chapter(n_clicks, text):
    if n_clicks and text:
        speak(text)
    return text

@app.callback(
    Output('chat-history', 'children'),
    [Input('send-btn', 'n_clicks'), Input('speak-btn', 'n_clicks')],
    [State('chat-input', 'value'), State('chapter-text', 'children'), State('selected-book', 'children')]
)
def update_chat(send_clicks, speak_clicks, user_input, chapter_text, book_name):
    user_id = "user1"
    if not book_name or not chapter_text:
        return "Select a book and chapter first"
    book = book_name.split("Selected: ")[1]
    c.execute("SELECT user_input, ai_response FROM interactions WHERE user_id=? AND book=?", (user_id, book))
    past = [f"You: {row[0]} | AI: {row[1]}" for row in c.fetchall()]
    
    if send_clicks or speak_clicks:
        if speak_clicks:
            user_input = get_voice_input()
        if user_input and "Error" not in user_input:
            response = generate_response(user_input, chapter_text, past)
            c.execute("INSERT INTO interactions (user_id, book, chapter, user_input, ai_response, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
                      (user_id, book, chapter_text[:50], user_input, response, datetime.now().isoformat()))
            conn.commit()
            past.append(f"You: {user_input} | AI: {response}")
    return html.Ul([html.Li(p) for p in past]) if past else "Start chatting!"

@app.callback(
    Output('fanfic-output', 'children'),
    Input('generate-fanfic-btn', 'n_clicks'),
    [State('fanfic-prompt', 'value'), State('visibility', 'value'), State('selected-book', 'children')]
)
def generate_fanfic(n_clicks, prompt, visibility, book_name):
    user_id = "user1"
    if n_clicks and prompt and book_name:
        book = book_name.split("Selected: ")[1]
        chapters = books[book]
        fanfic = generate_fanfiction(book, chapters, prompt)
        fanfic_text = "\n\n".join([f"Chapter {i+1}: {chapter}" for i, chapter in enumerate(fanfic)])
        c.execute("INSERT INTO fanfictions (user_id, book, prompt, text, public, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
                  (user_id, book, prompt, fanfic_text, 1 if visibility == 'Public' else 0, datetime.now().isoformat()))
        conn.commit()
        return html.Pre(fanfic_text)
    return "Enter a prompt to generate fanfiction"

@app.callback(
    Output('fanfic-library', 'children'),
    Input('generate-fanfic-btn', 'n_clicks')
)
def update_library(n_clicks):
    c.execute("SELECT book, prompt, text FROM fanfictions WHERE public=1")
    return html.Ul([html.Li(f"{row[0]} - {row[1]}: {row[2][:100]}...") for row in c.fetchall()])

@app.callback(
    [Output('streak-info', 'children'), Output('activity-graph', 'figure'), Output('recommendations', 'children')],
    Input('tabs', 'value')
)
def update_dashboard(tab):
    user_id = "user1"
    if tab != 'dashboard':
        return "", {}, ""
    
    # Update streaks
    today = datetime.now().date().isoformat()
    c.execute("SELECT days, last_login FROM streaks WHERE user_id=?", (user_id,))
    streak = c.fetchone()
    if streak:
        days, last = streak
        last_date = datetime.fromisoformat(last).date()
        if last != today:
            if (datetime.now().date() - last_date).days == 1:
                days += 1
            else:
                days = 1
            c.execute("UPDATE streaks SET days=?, last_login=? WHERE user_id=?", (days, today, user_id))
    else:
        days = 1
        c.execute("INSERT INTO streaks (user_id, days, last_login) VALUES (?, ?, ?)", (user_id, days, today))
    conn.commit()

    # Activity graph
    c.execute("SELECT timestamp FROM interactions WHERE user_id=?", (user_id,))
    dates = [datetime.fromisoformat(row[0]).date() for row in c.fetchall()]
    fig = go.Figure(data=[go.Histogram(x=dates, marker_color='#3498db')])

    # Recommendations
    c.execute("SELECT book FROM interactions WHERE user_id=?", (user_id,))
    books_read = [row[0] for row in c.fetchall()]
    recs = "Try 'Percy Jackson & The Lightning Thief'" if "Harry Potter" in str(books_read) else "Explore more fantasy!"

    return f"Streak: {days} days", fig, recs

if __name__ == '__main__':
    app.run(debug=True)