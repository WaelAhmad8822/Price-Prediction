"""
PythonAnywhere WSGI configuration file
This file is loaded by PythonAnywhere's web server
"""

import sys
import os

# Add the project directory to the Python path
project_home = os.path.expanduser('~/house-price-model')
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Change to project directory
os.chdir(project_home)

# Set environment to production
os.environ['FLASK_ENV'] = 'production'
os.environ['WERKZEUG_RUN_MAIN'] = 'true'

# Import the Flask app
try:
    from app import app as application
except ImportError as e:
    print(f"Error importing app: {e}")
    # Return a simple error application
    def application(environ, start_response):
        status = '500 Internal Server Error'
        response_headers = [('Content-Type', 'text/plain')]
        start_response(status, response_headers)
        return [b'Error: Could not import Flask application']

# Optional: Add request logging
def log_request(environ, start_response):
    """Middleware for logging requests"""
    path = environ.get('PATH_INFO', '/')
    method = environ.get('REQUEST_METHOD', 'GET')
    print(f"{method} {path}", flush=True)
    return application(environ, start_response)

# Use logging middleware
application = log_request
