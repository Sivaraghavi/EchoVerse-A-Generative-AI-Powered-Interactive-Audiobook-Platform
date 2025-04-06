# # import sqlite3
# # from datetime import datetime
# # from typing import List, Dict, Optional

# # # Initialize database connection
# # conn = sqlite3.connect('echoverse.db', check_same_thread=False)
# # cursor = conn.cursor()

# # # Create tables if they don't exist
# # def initialize_database():
# #     try:
# #         cursor.execute('''
# #             CREATE TABLE IF NOT EXISTS interactions (
# #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                 user_id TEXT NOT NULL,
# #                 book TEXT NOT NULL,
# #                 chapter TEXT NOT NULL,
# #                 user_input TEXT NOT NULL,
# #                 ai_response TEXT NOT NULL,
# #                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
# #             )
# #         ''')
        
# #         cursor.execute('''
# #             CREATE TABLE IF NOT EXISTS fanfictions (
# #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                 user_id TEXT NOT NULL,
# #                 book TEXT NOT NULL,
# #                 prompt TEXT NOT NULL,
# #                 text TEXT NOT NULL,
# #                 is_public BOOLEAN DEFAULT 1,
# #                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
# #             )
# #         ''')
        
# #         cursor.execute('''
# #             CREATE TABLE IF NOT EXISTS reading_streaks (
# #                 user_id TEXT PRIMARY KEY,
# #                 current_streak INTEGER DEFAULT 0,
# #                 longest_streak INTEGER DEFAULT 0,
# #                 last_activity_date DATE
# #             )
# #         ''')
        
# #         conn.commit()
# #     except sqlite3.Error as e:
# #         print(f"Database initialization error: {e}")

# # initialize_database()

# # def get_interactions(user_id: str, book: str) -> List[str]:
# #     """Get past interactions for a user and book"""
# #     try:
# #         cursor.execute('''
# #             SELECT user_input, ai_response 
# #             FROM interactions 
# #             WHERE user_id = ? AND book = ?
# #             ORDER BY timestamp DESC
# #             LIMIT 5
# #         ''', (user_id, book))
# #         return [f"You: {row[0]} | AI: {row[1]}" for row in cursor.fetchall()]
# #     except sqlite3.Error as e:
# #         print(f"Error getting interactions: {e}")
# #         return []

# # def save_interaction(user_id: str, book: str, chapter: str, 
# #                     user_input: str, ai_response: str) -> bool:
# #     """Save a user-AI interaction"""
# #     try:
# #         cursor.execute('''
# #             INSERT INTO interactions 
# #             (user_id, book, chapter, user_input, ai_response)
# #             VALUES (?, ?, ?, ?, ?)
# #         ''', (user_id, book, chapter, user_input, ai_response))
# #         conn.commit()
# #         return True
# #     except sqlite3.Error as e:
# #         print(f"Error saving interaction: {e}")
# #         return False

# # def save_fanfiction(user_id: str, book: str, prompt: str, 
# #                    text: str, is_public: bool) -> bool:
# #     """Save generated fanfiction"""
# #     try:
# #         cursor.execute('''
# #             INSERT INTO fanfictions 
# #             (user_id, book, prompt, text, is_public)
# #             VALUES (?, ?, ?, ?, ?)
# #         ''', (user_id, book, prompt, text, int(is_public)))
# #         conn.commit()
# #         return True
# #     except sqlite3.Error as e:
# #         print(f"Error saving fanfiction: {e}")
# #         return False

# # def get_public_fanfictions(limit: int = 10) -> List[Dict]:
# #     """Get public fanfictions for the library"""
# #     try:
# #         cursor.execute('''
# #             SELECT id, book, prompt, text, timestamp 
# #             FROM fanfictions 
# #             WHERE is_public = 1
# #             ORDER BY timestamp DESC
# #             LIMIT ?
# #         ''', (limit,))
# #         columns = [col[0] for col in cursor.description]
# #         return [dict(zip(columns, row)) for row in cursor.fetchall()]
# #     except sqlite3.Error as e:
# #         print(f"Error getting public fanfictions: {e}")
# #         return []

# # def update_reading_streak(user_id: str) -> bool:
# #     """Update user's reading streak"""
# #     try:
# #         today = datetime.now().date()
        
# #         # Get current streak
# #         cursor.execute('''
# #             SELECT current_streak, longest_streak, last_activity_date 
# #             FROM reading_streaks 
# #             WHERE user_id = ?
# #         ''', (user_id,))
# #         result = cursor.fetchone()
        
# #         if result:
# #             current_streak, longest_streak, last_date = result
# #             last_date = datetime.strptime(last_date, '%Y-%m-%d').date() if last_date else None
            
# #             if last_date:
# #                 days_since = (today - last_date).days
                
# #                 if days_since == 0:
# #                     return True  # Already updated today
# #                 elif days_since == 1:
# #                     current_streak += 1
# #                 else:
# #                     current_streak = 1
                
# #                 longest_streak = max(longest_streak, current_streak)
            
# #             cursor.execute('''
# #                 UPDATE reading_streaks 
# #                 SET current_streak = ?, longest_streak = ?, last_activity_date = ?
# #                 WHERE user_id = ?
# #             ''', (current_streak, longest_streak, today.isoformat(), user_id))
# #         else:
# #             cursor.execute('''
# #                 INSERT INTO reading_streaks 
# #                 (user_id, current_streak, longest_streak, last_activity_date)
# #                 VALUES (?, 1, 1, ?)
# #             ''', (user_id, today.isoformat()))
        
# #         conn.commit()
# #         return True
# #     except sqlite3.Error as e:
# #         print(f"Error updating reading streak: {e}")
# #         return False

# # def get_reading_streak(user_id: str) -> Dict[str, int]:
# #     """Get user's reading streak stats"""
# #     try:
# #         cursor.execute('''
# #             SELECT current_streak, longest_streak 
# #             FROM reading_streaks 
# #             WHERE user_id = ?
# #         ''', (user_id,))
# #         result = cursor.fetchone()
        
# #         if result:
# #             return {'current': result[0], 'longest': result[1]}
# #         return {'current': 0, 'longest': 0}
# #     except sqlite3.Error as e:
# #         print(f"Error getting reading streak: {e}")
# #         return {'current': 0, 'longest': 0}

# from dash import dcc, html

# def layout():
#     return html.Div([
#         html.Header(className='header', children=[
#             html.Button('☰', id='hamburger-btn', className='hamburger-btn'),
#             html.H1("EchoVerse", className='logo'),
#             # Upload PDF button moved to header
#             dcc.Upload(id='upload-pdf', children=html.Button('Upload PDF', className='upload-btn'), multiple=False)
#         ]),
#         html.Div(id='sidebar', className='sidebar hidden', children=[
#             dcc.Link("Home", href='/', className='nav-link'),
#             dcc.Link("Fanfiction", href='/fanfiction', className='nav-link'),
#             dcc.Link("Dashboard", href='/dashboard', className='nav-link')
#         ]),
#         dcc.Location(id='url', refresh=False),
#         html.Div(id='page-content', className='content', n_clicks=0),
#         html.Footer(className='footer', children=[
#             html.Div(className='social-developer-container', children=[
#                 html.Div(className='social-icons', children=[
#                     html.A(html.Img(src='/assets/github-icon.png', alt='GitHub'), href='#', target='_blank'),
#                     html.A(html.Img(src='/assets/linkedin-icon.png', alt='LinkedIn'), href='#', target='_blank'),
#                     html.A(html.Img(src='/assets/instagram-icon.png', alt='Instagram'), href='#', target='_blank'),
#                     html.A(html.Img(src='/assets/mail-icon.png', alt='Mail'), href='#', target='_blank'),
#                     html.A(html.Img(src='/assets/twitter-icon.png', alt='Twitter'), href='#', target='_blank')
#                 ]),
#                 html.Div(className='developer', children=[
#                     html.Img(src='/assets/developer_face.jpg', alt='Developer', className='developer-img'),
#                     html.P("About the Developer", className='developer-text')
#                 ])
#             ]),
#             html.P("© 2025 EchoVerse. All rights reserved.", className='copyright')
#         ])
#     ])

# def home_page():
#     return html.Div([
#         html.H1("Welcome to EchoVerse", className='welcome-message'),
#         dcc.Input(
#             id='search-input',
#             placeholder="Search for a book...",
#             className='search-bar'
#         ),
#         html.H2("Select a Book", className='title'),
#         html.Div(id='book-grid', className='book-grid')
#     ])

# def book_details_page(book_id):
#     # Find the book from the library
#     from callbacks import book_library  # Import library from callbacks
#     book = next((b for b in book_library if b["id"] == book_id), None)
#     if not book:
#         return html.Div("Book not found.")
#     return html.Div([
#         html.H1(book["title"], className='book-title'),
#         html.Img(src=f'/assets/{book["cover"]}', className='book-cover-large'),
#         dcc.Dropdown(id='chapter-select', options=[], placeholder="Select a Chapter", className='chapter-dropdown'),
#         html.P(id='chapter-text', className='chapter-text'),
#         html.Button("🎙️ Narrate", id='narrate-btn', className='narrate-btn'),
#         html.H3("Chat with AI Buddy", className='chat-title'),
#         html.Button("🎤 Speak", id='speak-btn', className='speak-btn'),
#         dcc.Textarea(id='chat-input', placeholder="Or type here...", className='chat-input'),
#         html.Button("Send", id='send-btn', className='send-btn'),
#         html.Div(id='chat-history', className='chat-history')
#     ])

# def fanfiction_page():
#     return html.Div([
#         html.H1("Create Fanfiction", className='title'),
#         dcc.Textarea(id='fanfic-prompt', placeholder="E.g., 'What if Harry and Ron were dating?'", className='fanfic-prompt'),
#         dcc.RadioItems(id='visibility', options=['Public', 'Private'], value='Private', inline=True, className='visibility'),
#         html.Button("✨ Generate", id='generate-fanfic-btn', className='generate-btn'),
#         html.Div(id='fanfic-output', className='fanfic-output'),
#         html.H2("Fanfiction Library", className='library-title'),
#         html.Div(id='fanfic-library', className='fanfic-library')
#     ])

# def dashboard_page():
#     return html.Div([
#         html.H1("Your Dashboard", className='title'),
#         html.Div(className='streak-calendar', id='streak-calendar'),
#         dcc.Graph(id='activity-graph', className='activity-graph'),
#         html.H2("Recommended Books", className='recs-title'),
#         html.P(id='recommendations', className='recommendations')
#     ])

import sqlite3
from datetime import datetime

conn = sqlite3.connect('echoverse.db', check_same_thread=False)
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS interactions (
        user_id TEXT, 
        book TEXT, 
        chapter TEXT, 
        user_input TEXT, 
        ai_response TEXT, 
        timestamp TEXT
    )
''')
c.execute('''
    CREATE TABLE IF NOT EXISTS fanfictions (
        user_id TEXT, 
        book TEXT, 
        prompt TEXT, 
        text TEXT, 
        public INTEGER, 
        timestamp TEXT
    )
''')
c.execute('''
    CREATE TABLE IF NOT EXISTS streaks (
        user_id TEXT, 
        days INTEGER, 
        last_login TEXT
    )
''')
conn.commit()

def get_interactions(user_id, book):
    c.execute("SELECT user_input, ai_response FROM interactions WHERE user_id=? AND book=?", (user_id, book))
    return [f"You: {row[0]} | AI: {row[1]}" for row in c.fetchall()]

def save_interaction(user_id, book, chapter, user_input, ai_response):
    c.execute("INSERT INTO interactions VALUES (?, ?, ?, ?, ?, ?)",
              (user_id, book, chapter, user_input, ai_response, datetime.now().isoformat()))
    conn.commit()

def save_fanfiction(user_id, book, prompt, text, visibility):
    c.execute("INSERT INTO fanfictions VALUES (?, ?, ?, ?, ?, ?)",
              (user_id, book, prompt, text, 1 if visibility == 'Public' else 0, datetime.now().isoformat()))
    conn.commit()

def get_public_fanfictions():
    c.execute("SELECT book, prompt, text FROM fanfictions WHERE public=1")
    return [{'book': row[0], 'prompt': row[1], 'text': row[2]} for row in c.fetchall()]

def update_streaks(user_id):
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
        c.execute("INSERT INTO streaks VALUES (?, ?, ?)", (user_id, 1, today))
    conn.commit()

def get_streaks(user_id):
    c.execute("SELECT days FROM streaks WHERE user_id=?", (user_id,))
    result = c.fetchone()
    return result[0] if result else 0

def get_activity(user_id):
    c.execute("SELECT book, COUNT(*) FROM interactions WHERE user_id=? GROUP BY book", (user_id,))
    return {row[0]: row[1] for row in c.fetchall()}
