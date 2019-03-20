from flask import Flask, render_template

app = flask(__name__)

title = "Jinja Practice"

@app.route('/')
def index():
    render_template('home.html')

