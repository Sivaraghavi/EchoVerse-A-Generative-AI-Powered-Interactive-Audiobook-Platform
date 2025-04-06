# from dash import dcc, html
# import dash_bootstrap_components as dbc

# def layout():
#     return html.Div([
#         dcc.Location(id='url', refresh=False),
#         html.Div(id='page-content'),
        
#         # Hidden div to store temporary data
#         dcc.Store(id='session-data', storage_type='session'),
        
#         # Global loading spinner
#         dcc.Loading(
#             id="loading-global",
#             type="circle",
#             children=html.Div(id="loading-output")
#         )
#     ], className='app-container')

# def home_page():
#     return html.Div([
#         html.Header(className='app-header', children=[
#             html.H1("EchoVerse", className='app-title'),
#             html.Div(className='app-subtitle', children="AI-Powered Interactive Audiobooks")
#         ]),
        
#         dbc.Container([
#             dbc.Row([
#                 dbc.Col([
#                     dcc.Input(
#                         id='search-books',
#                         type='text',
#                         placeholder='🔍 Search for books...',
#                         className='search-input'
#                     )
#                 ], width=12)
#             ]),
            
#             html.H2("Featured Books", className='section-title'),
            
#             dbc.Row([
#                 dbc.Col([
#                     dbc.Card([
#                         dbc.CardImg(
#                             src="/assets/harry_potter_and_the_sorcerers_stone.jpg",
#                             top=True,
#                             className='book-cover'
#                         ),
#                         dbc.CardBody([
#                             html.H4("Harry Potter and the Sorcerer's Stone", className='book-title'),
#                             dbc.Button(
#                                 "Explore",
#                                 id='hp-button',
#                                 href="/book/Harry%20Potter%20and%20the%20Sorcerer%E2%80%99s%20Stone",
#                                 className='explore-button'
#                             )
#                         ])
#                     ], className='book-card')
#                 ], md=4),
                
#                 dbc.Col([
#                     dbc.Card([
#                         dbc.CardImg(
#                             src="/assets/percy_jackson_&_the_lightning_thief.jpg",
#                             top=True,
#                             className='book-cover'
#                         ),
#                         dbc.CardBody([
#                             html.H4("Percy Jackson & The Lightning Thief", className='book-title'),
#                             dbc.Button(
#                                 "Explore",
#                                 id='pj-button',
#                                 href="/book/Percy%20Jackson%20%26%20The%20Lightning%20Thief",
#                                 className='explore-button'
#                             )
#                         ])
#                     ], className='book-card')
#                 ], md=4),
                
#                 dbc.Col([
#                     dbc.Card([
#                         dbc.CardImg(
#                             src="/assets/logo.png",  # Placeholder for additional books
#                             top=True,
#                             className='book-cover'
#                         ),
#                         dbc.CardBody([
#                             html.H4("Upload Your Own Book", className='book-title'),
#                             dcc.Upload(
#                                 id='upload-book',
#                                 children=dbc.Button(
#                                     "Upload PDF",
#                                     className='upload-button'
#                                 ),
#                                 multiple=False
#                             )
#                         ])
#                     ], className='book-card')
#                 ], md=4)
#             ])
#         ], className='main-container'),
        
#         footer()
#     ])

# def book_details_page(book_name):
#     return html.Div([
#         html.Header(className='app-header', children=[
#             html.H1("EchoVerse", className='app-title'),
#             html.Div(className='app-subtitle', children=f"Exploring: {book_name}")
#         ]),
        
#         dbc.Container([
#             dbc.Row([
#                 dbc.Col([
#                     html.Img(
#                         src=f"/assets/{book_name.replace(' ', '_').lower()}.jpg",
#                         className='book-detail-cover'
#                     )
#                 ], md=4),
                
#                 dbc.Col([
#                     html.H2(book_name, className='book-detail-title'),
#                     html.Div(className='book-meta', children=[
#                         html.Span("Fantasy", className='genre-tag'),
#                         html.Span("300 pages", className='page-count')
#                     ]),
                    
#                     dcc.Dropdown(
#                         id='chapter-selector',
#                         options=[
#                             {'label': 'Chapter 1', 'value': 0},
#                             {'label': 'Chapter 2', 'value': 1}
#                         ],
#                         placeholder="Select a chapter...",
#                         className='chapter-dropdown'
#                     ),
                    
#                     html.Div(id='chapter-content', className='chapter-content'),
                    
#                     dbc.ButtonGroup([
#                         dbc.Button(
#                             "🎧 Narrate Chapter",
#                             id='narrate-button',
#                             className='action-button'
#                         ),
#                         dbc.Button(
#                             "📖 Read Aloud",
#                             id='read-button',
#                             className='action-button'
#                         )
#                     ], className='action-button-group')
#                 ], md=8)
#             ]),
            
#             html.Hr(),
            
#             html.H3("Discuss with AI Buddy", className='section-title'),
            
#             dbc.Row([
#                 dbc.Col([
#                     dcc.Textarea(
#                         id='chat-input',
#                         placeholder='Ask about this chapter or book...',
#                         className='chat-input'
#                     ),
                    
#                     dbc.ButtonGroup([
#                         dbc.Button(
#                             "🎤 Speak",
#                             id='voice-input-button',
#                             className='voice-button'
#                         ),
#                         dbc.Button(
#                             "✉️ Send",
#                             id='send-message-button',
#                             className='send-button'
#                         )
#                     ], className='chat-button-group')
#                 ], md=8),
                
#                 dbc.Col([
#                     html.Div(id='chat-history', className='chat-history')
#                 ], md=4)
#             ]),
            
#             html.Hr(),
            
#             html.H3("Create Fanfiction", className='section-title'),
            
#             dbc.Row([
#                 dbc.Col([
#                     dcc.Textarea(
#                         id='fanfiction-prompt',
#                         placeholder='What if... (describe your alternate story idea)',
#                         className='fanfiction-input'
#                     ),
                    
#                     dbc.RadioItems(
#                         id='fanfiction-visibility',
#                         options=[
#                             {'label': 'Public', 'value': 'public'},
#                             {'label': 'Private', 'value': 'private'}
#                         ],
#                         value='public',
#                         inline=True,
#                         className='visibility-options'
#                     ),
                    
#                     dbc.Button(
#                         "✨ Generate Fanfiction",
#                         id='generate-fanfiction-button',
#                         className='generate-button'
#                     )
#                 ], md=8),
                
#                 dbc.Col([
#                     html.Div(id='fanfiction-output', className='fanfiction-output')
#                 ], md=4)
#             ])
#         ], className='main-container'),
        
#         footer()
#     ])

# def fanfiction_page():
#     return html.Div([
#         html.Header(className='app-header', children=[
#             html.H1("EchoVerse", className='app-title'),
#             html.Div(className='app-subtitle', children="Fanfiction Library")
#         ]),
        
#         dbc.Container([
#             dbc.Row([
#                 dbc.Col([
#                     html.H2("Community Creations", className='section-title'),
#                     html.Div(id='fanfiction-library', className='fanfiction-library')
#                 ], md=8),
                
#                 dbc.Col([
#                     html.H2("Your Fanfictions", className='section-title'),
#                     html.Div(id='user-fanfictions', className='user-fanfictions')
#                 ], md=4)
#             ])
#         ], className='main-container'),
        
#         footer()
#     ])

# def dashboard_page():
#     return html.Div([
#         html.Header(className='app-header', children=[
#             html.H1("EchoVerse", className='app-title'),
#             html.Div(className='app-subtitle', children="Your Reading Dashboard")
#         ]),
        
#         dbc.Container([
#             dbc.Row([
#                 dbc.Col([
#                     html.H2("Reading Streak", className='section-title'),
#                     html.Div(id='streak-calendar', className='streak-calendar')
#                 ], md=4),
                
#                 dbc.Col([
#                     html.H2("Your Activity", className='section-title'),
#                     dcc.Graph(id='activity-graph', className='activity-graph')
#                 ], md=8)
#             ]),
            
#             dbc.Row([
#                 dbc.Col([
#                     html.H2("Recommended Books", className='section-title'),
#                     html.Div(id='book-recommendations', className='book-recommendations')
#                 ], md=12)
#             ])
#         ], className='main-container'),
        
#         footer()
#     ])

# def footer():
#     return html.Footer(className='app-footer', children=[
#         dbc.Container([
#             dbc.Row([
#                 dbc.Col([
#                     html.H4("Connect With Us", className='footer-title'),
#                     html.Div(className='social-links', children=[
#                         html.A(
#                             html.Img(src="/assets/githubicon.png", className='social-icon'),
#                             href="https://github.com/yourusername",
#                             target="_blank"
#                         ),
#                         html.A(
#                             html.Img(src="/assets/linkedinicon.png", className='social-icon'),
#                             href="https://linkedin.com/in/yourprofile",
#                             target="_blank"
#                         ),
#                         html.A(
#                             html.Img(src="/assets/twittericon.png", className='social-icon'),
#                             href="https://twitter.com/yourhandle",
#                             target="_blank"
#                         ),
#                         html.A(
#                             html.Img(src="/assets/mailicon.png", className='social-icon'),
#                             href="mailto:youremail@example.com"
#                         )
#                     ])
#                 ], md=4),
                
#                 dbc.Col([
#                     html.H4("About EchoVerse", className='footer-title'),
#                     html.P("An AI-powered interactive audiobook platform that brings stories to life with generative AI and voice technology.", className='footer-description')
#                 ], md=4),
                
#                 dbc.Col([
#                     html.H4("Developer", className='footer-title'),
#                     html.Div(className='developer-info', children=[
#                         html.Img(
#                             src="/assets/developerface.jpg",
#                             className='developer-image'
#                         ),
#                         html.Div([
#                             html.P("Created by Your Name", className='developer-name'),
#                             html.P("AI & Voice Technology Enthusiast", className='developer-title')
#                         ])
#                     ])
#                 ], md=4)
#             ]),
            
#             html.Hr(className='footer-divider'),
            
#             html.P("© 2025 EchoVerse. All rights reserved.", className='copyright')
#         ])
#     ])

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