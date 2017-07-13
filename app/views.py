# views.py

from flask import render_template

from app import app

""" landing page - which happens to also be the registration page """

@app.route('/')
def index():
    return render_template("index.html")

""" we handle user registration """

@app.route('/register')
def signup_page():
    return render_template("index.html")
    
@app.route('/register')
def create_user():
    return render_template("index.html")
    
""" we handle user login and logout """

@app.route('/signin')
def signin_page():
    return render_template("sign_in.html")
    
""" we handle bucket operations """
    
@app.route('/buckets')
def view_buckets():
    return render_template("buckets.html")
    
""" we handle goal operations """
    
@app.route('/goals')
def view_goals():
    return render_template("goals.html")