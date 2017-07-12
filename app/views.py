# views.py

from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signin')
def about():
    return render_template("sign_in.html")