from flask import Flask, render_template

app = Flask(__name__)

title = "Jinja Practice"

@app.route('/')
def index():
    render_template('home.html', title=title)

@app.route('/about')
def about():
    render_template('about.html', title=title)

if __name__ == "__main__":
    app.run(debug=True)