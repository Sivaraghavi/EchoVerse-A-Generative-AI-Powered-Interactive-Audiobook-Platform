from dash import dcc, html

def layout():
    return html.Div([
        html.Header(className='header', children=[
            html.Button('☰', id='hamburger-btn', className='hamburger-btn'),
            html.H1("EchoVerse", className='logo'),
            # Upload PDF button moved to header
            dcc.Upload(id='upload-pdf', children=html.Button('Upload PDF', className='upload-btn'), multiple=False)
        ]),
        html.Div(id='sidebar', className='sidebar hidden', children=[
            dcc.Link("Home", href='/', className='nav-link'),
            dcc.Link("Fanfiction", href='/fanfiction', className='nav-link'),
            dcc.Link("Dashboard", href='/dashboard', className='nav-link')
        ]),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content', className='content', n_clicks=0),
        html.Footer(className='footer', children=[
            html.Div(className='social-developer-container', children=[
                html.Div(className='social-icons', children=[
                    html.A(html.Img(src='/assets/github-icon.png', alt='GitHub'), href='#', target='_blank'),
                    html.A(html.Img(src='/assets/linkedin-icon.png', alt='LinkedIn'), href='#', target='_blank'),
                    html.A(html.Img(src='/assets/instagram-icon.png', alt='Instagram'), href='#', target='_blank'),
                    html.A(html.Img(src='/assets/mail-icon.png', alt='Mail'), href='#', target='_blank'),
                    html.A(html.Img(src='/assets/twitter-icon.png', alt='Twitter'), href='#', target='_blank')
                ]),
                html.Div(className='developer', children=[
                    html.Img(src='/assets/developer_face.jpg', alt='Developer', className='developer-img'),
                    html.P("About the Developer", className='developer-text')
                ])
            ]),
            html.P("© 2025 EchoVerse. All rights reserved.", className='copyright')
        ])
    ])

def home_page():
    return html.Div([
        html.H1("Welcome to EchoVerse", className='welcome-message'),
        dcc.Input(
            id='search-input',
            placeholder="Search for a book...",
            className='search-bar'
        ),
        html.H2("Select a Book", className='title'),
        html.Div(id='book-grid', className='book-grid')
    ])

def book_details_page(book_id):
    # Find the book from the library
    from callbacks import book_library  # Import library from callbacks
    book = next((b for b in book_library if b["id"] == book_id), None)
    if not book:
        return html.Div("Book not found.")
    return html.Div([
        html.H1(book["title"], className='book-title'),
        html.Img(src=f'/assets/{book["cover"]}', className='book-cover-large'),
        dcc.Dropdown(id='chapter-select', options=[], placeholder="Select a Chapter", className='chapter-dropdown'),
        html.P(id='chapter-text', className='chapter-text'),
        html.Button("🎙️ Narrate", id='narrate-btn', className='narrate-btn'),
        html.H3("Chat with AI Buddy", className='chat-title'),
        html.Button("🎤 Speak", id='speak-btn', className='speak-btn'),
        dcc.Textarea(id='chat-input', placeholder="Or type here...", className='chat-input'),
        html.Button("Send", id='send-btn', className='send-btn'),
        html.Div(id='chat-history', className='chat-history')
    ])

def fanfiction_page():
    return html.Div([
        html.H1("Create Fanfiction", className='title'),
        dcc.Textarea(id='fanfic-prompt', placeholder="E.g., 'What if Harry and Ron were dating?'", className='fanfic-prompt'),
        dcc.RadioItems(id='visibility', options=['Public', 'Private'], value='Private', inline=True, className='visibility'),
        html.Button("✨ Generate", id='generate-fanfic-btn', className='generate-btn'),
        html.Div(id='fanfic-output', className='fanfic-output'),
        html.H2("Fanfiction Library", className='library-title'),
        html.Div(id='fanfic-library', className='fanfic-library')
    ])

def dashboard_page():
    return html.Div([
        html.H1("Your Dashboard", className='title'),
        html.Div(className='streak-calendar', id='streak-calendar'),
        dcc.Graph(id='activity-graph', className='activity-graph'),
        html.H2("Recommended Books", className='recs-title'),
        html.P(id='recommendations', className='recommendations')
    ])
