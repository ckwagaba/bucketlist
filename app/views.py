# views.py

from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/signin')
def signin():
    return render_template("sign_in.html")
    
@app.route('/register')
def signup():
    return render_template("index.html")
    
@app.route('/buckets')
def buckets():
    return render_template("buckets.html")
    
@app.route('/goals')
def goals():
    return render_template("goals.html")