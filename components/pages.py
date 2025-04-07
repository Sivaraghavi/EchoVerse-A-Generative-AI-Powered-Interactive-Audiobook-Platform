# # # components/pages.py
# # from dash import dcc, html
# # import dash_bootstrap_components as dbc

# # def home_page():
# #     return html.Div([
# #         # Your home page content here
# #         html.H1("Welcome to EchoVerse"),
# #         # ... rest of your home page implementation
# #     ])

# # def book_details_page(book_name):
# #     return html.Div([
# #         # Your book details page content here
# #         html.H1(f"Book: {book_name}"),
# #         # ... rest of your book details implementation
# #     ])

# # def fanfiction_page():
# #     return html.Div([
# #         # Your fanfiction page content here
# #         html.H1("Fanfiction Creation"),
# #         # ... rest of your fanfiction page implementation
# #     ])

# # def dashboard_page():
# #     return html.Div([
# #         # Your dashboard page content here
# #         html.H1("Your Dashboard"),
# #         # ... rest of your dashboard implementation
# #     ])

# # def footer():
# #     return html.Footer([
# #         # Your footer content here
# #         html.P("© 2025 EchoVerse")
# #     ])

# from dash import dcc, html
# import dash_bootstrap_components as dbc

# def home_page():
#     return html.Div([
#         html.Div(className='header', children=[
#             html.Span('EchoVerse', className='logo'),
#             dcc.Upload(html.Button('Upload', className='uploadbtn'), id='upload-book')
#         ]),
#         html.H1('Welcome to EchoVerse', className='welcomemessage'),
#         dcc.Input(id='search-bar', type='text', placeholder='Search books...', className='searchbar'),
#         html.Div(className='bookgrid', children=[
#             html.Div(className='bookcard', children=[
#                 html.Img(src='/assets/logo.png', className='bookcover'),
#                 html.H3('Sample Book 1', className='booktitle'),
#                 html.A('Select', href='/book/Sample%20Book%201', className='selectbtn')
#             ]),
#             html.Div(className='bookcard', children=[
#                 html.Img(src='/assets/logo.png', className='bookcover'),
#                 html.H3('Sample Book 2', className='booktitle'),
#                 html.A('Select', href='/book/Sample%20Book%202', className='selectbtn')
#             ])
#         ]),
#         footer()
#     ])

# def book_details_page(book_name):
#     return html.Div([
#         html.Div(className='header', children=[
#             html.Span('EchoVerse', className='logo')
#         ]),
#         html.Img(src='/assets/logo.png', className='bookcoverlarge'),
#         html.H2(book_name, className='title'),
#         dcc.Dropdown(
#             id='chapter-dropdown',
#             options=[{'label': f'Chapter {i}', 'value': i} for i in range(1, 3)],
#             value=1,
#             className='chapterdropdown'
#         ),
#         html.Div(id='chapter-text', className='chaptertext'),
#         html.Button('Narrate', id='narrate-btn', className='narratebtn'),
#         html.H3('Chat with AI Buddy', className='chattitle'),
#         dcc.Textarea(id='chat-input', placeholder='Ask about the book...', className='chatinput'),
#         html.Button('Speak', id='speak-btn', className='speakbtn'),
#         html.Button('Send', id='send-btn', className='sendbtn'),
#         html.Div(id='chat-history', className='chathistory'),
#         html.H3('Create Fanfiction', className='title'),
#         dcc.Textarea(id='fanfic-prompt', placeholder='Your fanfiction idea...', className='fanficprompt'),
#         dbc.RadioItems(
#             id='fanfic-visibility',
#             options=[{'label': 'Public', 'value': 'public'}, {'label': 'Private', 'value': 'private'}],
#             value='public',
#             inline=True,
#             className='visibility'
#         ),
#         html.Button('Generate', id='generate-btn', className='generatebtn'),
#         html.Div(id='fanfic-output', className='fanficoutput'),
#         footer()
#     ])

# def fanfiction_page():
#     return html.Div([
#         html.Div(className='header', children=[
#             html.Span('EchoVerse', className='logo')
#         ]),
#         html.H2('Fanfiction Library', className='librarytitle'),
#         html.Div(id='fanfic-library', className='fanficlibrary'),
#         footer()
#     ])

# def dashboard_page():
#     return html.Div([
#         html.Div(className='header', children=[
#             html.Span('EchoVerse', className='logo')
#         ]),
#         html.H2('Reading Streak', className='title'),
#         html.Div(id='streak-calendar', className='streakcalendar'),
#         html.H2('Activity Graph', className='title'),
#         dcc.Graph(id='activity-graph', className='activitygraph'),
#         html.H2('Recommendations', className='recstitle'),
#         html.Div(id='recommendations', className='recommendations'),
#         footer()
#     ])

# def footer():
#     return html.Footer(className='footer', children=[
#         html.Div(className='socialdevelopercontainer', children=[
#             html.Div(className='socialicons', children=[
#                 html.A(html.Img(src='/assets/githubicon.png'), href='https://github.com/yourusername', target='_blank'),
#                 html.A(html.Img(src='/assets/linkedinicon.png'), href='https://linkedin.com/in/yourprofile', target='_blank'),
#                 html.A(html.Img(src='/assets/twittericon.png'), href='https://twitter.com/yourhandle', target='_blank'),
#                 html.A(html.Img(src='/assets/mailicon.png'), href='mailto:youremail@example.com')
#             ]),
#             html.Div(className='developer', children=[
#                 html.Img(src='/assets/developerface.jpg', className='developerimg'),
#                 html.Div(className='developertext', children=[
#                     html.P('Created by Your Name'),
#                     html.P('AI & Voice Tech Enthusiast')
#                 ])
#             ])
#         ]),
#         html.P('© 2025 EchoVerse', className='copyright')
#     ])