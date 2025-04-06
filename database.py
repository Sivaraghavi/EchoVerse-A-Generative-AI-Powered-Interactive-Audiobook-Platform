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
