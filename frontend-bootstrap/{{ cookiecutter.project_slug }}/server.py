"""
@file server.py

@brief Does web server things

@author Christopher Su
"""

import argparse
import os

from flask import Flask, request, render_template, send_from_directory
app = Flask(__name__)
app.config['SITE_TITLE'] = 'Website Title'

# Render template
@app.route('/')
def index():
  return render_template('home.html', title='Hello, World')

# URL parameter
@app.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username):
  return 'User %s' % username

# Request data
@app.route('/grant', methods=['POST'])
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