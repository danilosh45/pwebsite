from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/projects')
def link():
    return render_template("link.html")

@app.route('/photo')
def home():
    return render_template("home.html")
