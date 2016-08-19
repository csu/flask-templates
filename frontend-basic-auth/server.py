"""
@file server.py

@brief Does web server things

@author Christopher Su
"""

import argparse

from functools import wraps
from flask import Flask, request, render_template, Response
app = Flask(__name__)

def check_auth(username, password):
    return username == 'admin' and password == 'secret'

def authenticate():
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

# Render template
@app.route('/')
def index():
  return render_template('home.html', title='Hello, World')

# URL parameter
@app.route('/admin', methods=['GET'])
@requires_auth
def admin():
  return 'Admin'

# Request data
@app.route('/api/new', methods=['POST'])
@requires_auth
def grant_achievement():
  assert request.form['thing']
  return 'Hi'

# Favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='The Achieve web server.')
  parser.add_argument('--debug', dest='debug', action='store_true')
  parser.set_defaults(debug=False)
  args = parser.parse_args()

  app.run(debug=args.debug)