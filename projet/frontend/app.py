from flask import Flask, render_template
import os

frontend_app = Flask(__name__)

@frontend_app.route('/')
def serve_homepage():
    # Render the index.html file from the templates folder
    return render_template('index.html')

@frontend_app.route('/about')
def about():
    # Add a new route to serve an about page
    return "Welcome to the About Page!"

if __name__ == '__main__':
    frontend_app.run(host='0.0.0.0', port=5000)