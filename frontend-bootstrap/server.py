"""
@file server.py

@brief Does web server things

@author Christopher Su
"""

from flask import Flask, request, render_template
app = Flask(__name__)

# Render template
@app.route('/')
def index():
  return render_template('index.html', title='Hello, World')

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
  app.run()