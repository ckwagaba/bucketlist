# import required modules

from flask import render_template, redirect, url_for, request, session
from app import app
from functionality.user import *
from functionality.buckets import *
from functionality.goals import *

# making the user object available to all
all_users = []

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
    global all_users # global user object to store credentials
    if request.method == 'POST': # proper form submission
        # get values from request
        name = request.form['user_name']
        email = request.form['user_email']
        password = request.form['user_password']
        # update global user object with values
        this_user = User(name, email, password, [])
        # then redirect to sign in
        return redirect('/signin')
    else: # show registration form
        return redirect('/register')
    
""" we handle user login and logout """

@app.route('/signin')
def signin_page():
    return render_template("sign_in.html")
    
@app.route('/signin', methods = ['POST', 'GET'])
def login():
    global all_users
    if request.method == 'POST': # proper form submission
        # get values from request
        email = request.form['user_email']
        password = request.form['user_password']
        # Authenticate user
        login_token = this_user.login(email, password)
        if login_token == 1: # successful login
            return redirect('/buckets')
        else: # unsuccessful login
            return redirect('/signin')
    else: # show login form
        return redirect('/signin')
        
@app.route('/logout')
def logout():
    return redirect('/signin')
    
""" we handle bucket operations """
    
@app.route('/buckets')
def view_buckets():
    global all_users
    this_user_name = this_user.user_name
    this_user_buckets = this_user.user_buckets
    return render_template("buckets.html", user_name = this_user_name, user_buckets = this_user_buckets)
    

    
@app.route('/create_bucket')
def create_bucket_page():
    return render_template("create_bucket.html")
    
@app.route('/create_bucket', methods = ['POST', 'GET'])
def create_bucket_list():
    global all_users
    if request.method == 'POST': # proper form submission
        # get values from request
        bucket_name = request.form['bucket_name']
        this_user.create_bucket(bucket_name)
        return redirect('/buckets')
    else: # show create bucket form
        return redirect('/create_bucket')
    
""" we handle goal operations """
    
@app.route('/goals')
def view_goals():
    return render_template("goals.html")
    
@app.route('/create_goal')
def create_goals_page():
    return render_template("create_goal.html")
    
@app.route('/create_goal', methods = ['POST', 'GET'])
def create_goals():
    return 'Still to handle this and more. But the functionality and tests for it exist. Thanks.'