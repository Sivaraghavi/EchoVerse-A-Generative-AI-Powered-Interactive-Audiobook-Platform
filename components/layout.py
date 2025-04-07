# # # components/layout.py
# # from dash import dcc, html
# # import dash_bootstrap_components as dbc

# # def layout():
# #     return html.Div([
# #         dcc.Location(id='url', refresh=False),
# #         dcc.Store(id='session-store', storage_type='session'),
# #         dcc.Store(id='temp-store'),
# #         dcc.Loading(
# #             id="loading-global",
# #             type="circle",
# #             color="#FF0000",
# #             children=html.Div(id="loading-output")
# #         ),
# #         html.Div(id='page-content')
# #     ], className='app-container')

# from dash import dcc, html

# def layout():
#     return html.Div([
#         dcc.Location(id='url', refresh=False),
#         dcc.Store(id='session-store', storage_type='session'),
#         html.Button('☰', id='hamburger-btn', className='hamburgerbtn'),
#         html.Div([
#             html.A('Home', href='/', className='navlink'),
#             html.A('Fanfiction', href='/fanfiction', className='navlink'),
#             html.A('Dashboard', href='/dashboard', className='navlink'),
#         ], id='sidebar', className='sideBar hidden'),
#         html.Div(id='page-content', className='content'),
#         dcc.Loading(
#             id="loading-global",
#             type="circle",
#             color="#FF0000",
#             children=html.Div(id="loading-output")
#         )
#     ])