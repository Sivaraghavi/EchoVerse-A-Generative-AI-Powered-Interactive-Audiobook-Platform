#!/usr/bin/env python
from app import app
import os

if __name__ == "__main__":
    # Ensure the assets directory exists
    if not os.path.exists('assets'):
        os.makedirs('assets')
    
    # Run the app
    app.run(
    debug=True,
    host='0.0.0.0',
    port=8050,
    dev_tools_hot_reload=True
)