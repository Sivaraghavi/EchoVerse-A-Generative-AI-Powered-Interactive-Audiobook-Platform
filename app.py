# # import dash
# # from dash import html
# # from components import layout
# # import os

# # # Initialize the app
# # # app = dash.Dash(
# # #     __name__,
# # #     suppress_callback_exceptions=True,
# # #     assets_folder='assets',
# # #     assets_url_path='assets',
# # #     meta_tags=[
# # #         {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
# # #     ]
# # # )
# # # In app.py, add explicit CSS:
# # app = dash.Dash(__name__, external_stylesheets=[
# #     'https://codepen.io/chriddyp/pen/bWLwgP.css'
# # ])

# # app.title = "EchoVerse - AI-Powered Interactive Audiobooks"
# # app._favicon = "logo.png"

# # # Use our custom index template
# # # app.index_string = open('templates/index.html', 'r').read()

# # # Define the app layout
# # app.layout = layout()

# # if __name__ == "__main__":
# #     # Ensure assets directory exists
# #     if not os.path.exists('assets'):
# #         os.makedirs('assets')
    
# #     # Run the app
# #     app = dash.Dash(__name__)
# #     app.layout = html.Div("Hello World", style={'color': 'white'})
# #     app.run(debug=True)
    
# import dash
# import os
# from components import layout

# # Initialize the Dash app
# app = dash.Dash(
#     __name__,
#     suppress_callback_exceptions=True,
#     assets_folder='assets',
#     meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1.0"}]
# )
# app.title = "EchoVerse - AI-Powered Interactive Audiobooks"
# app._favicon = "logo.png"

# # Set the layout from components
# app.layout = layout()

# if __name__ == "__main__":
#     # Ensure assets directory exists
#     if not os.path.exists('assets'):
#         os.makedirs('assets')
#     app.run(debug=True)

import dash
from dash import html, dcc
import callbacks  # Imports callbacks so they're registered
from components import layout

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=['/assets/style.css']
)

app.layout = layout()

if __name__ == '__main__':
    app.run(debug=True)
