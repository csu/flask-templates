"""
@file server.py

@brief Does web server things

@author Christopher Su
"""

import argparse

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello, World!'

# URL parameter
@app.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username):
  return 'User %s' % username

# Request data
@app.route('/grant', methods=['POST'])
def grant_achievement():
  assert request.form['thing']
  return 'Hi'

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='The Achieve web server.')
  parser.add_argument('--debug', dest='debug', action='store_true')
  parser.set_defaults(debug=False)
  args = parser.parse_args()

  app.run(debug=args.debug)