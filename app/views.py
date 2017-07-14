# import required modules

from flask import render_template, redirect, url_for, request
from app import app
from functionality.user import *
from functionality.buckets import *
from functionality.goals import *

# making the user object available to all
this_user = {}

""" landing page - which happens to also be the registration page """

@app.route('/')
def index():
    return render_template("index.html")

""" we handle user registration """

@app.route('/register')
def signup_page():
    return render_template("index.html")
    
@app.route('/register', methods = ['POST', 'GET'])
def create_user():
    if request.method == 'POST': # proper form submission
        # get values from request
        name = request.form['user_name']
        email = request.form['user_email']
        password = request.form['user_password']
        # create user with values
        this_user = User(name, email, password, [])
        return this_user
    else: # hot urls
        
        name = request.form['user_name']
        email = request.form['user_email']
        password = request.form['user_password']
        
        this_user = User(name, email, password, [])
        return this_user
    
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