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
        this_user_name = this_user.user_name
        return redirect('/signin')
        #return redirect(url_for('view_buckets', user_name = this_user_name))
    else: # hot urls
        
        name = request.form['user_name']
        email = request.form['user_email']
        password = request.form['user_password']
        
        this_user = User(name, email, password, [])
        this_user_name = this_user.user_name
        return redirect('/signin')
        #return redirect(url_for('view_buckets', user_name = this_user_name))
    
""" we handle user login and logout """

@app.route('/signin')
def signin_page():
    return render_template("sign_in.html")
    
@app.route('/signin', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST': # proper form submission
        # get values from request
        email = request.form['user_email']
        password = request.form['user_password']
        # sign in user with values
        this_user.login(email, password)
        this_user_name = this_user.user_name
        return redirect(url_for('view_buckets', user_name = this_user_name))
    else: # hot urls
        email = request.form['user_email']
        password = request.form['user_password']
        
        this_user.login(email, password)
        this_user_name = this_user.user_name
        return redirect(url_for('view_buckets', user_name = this_user_name))
    
""" we handle bucket operations """
    
@app.route('/buckets')
def view_buckets():
    return render_template("buckets.html")
    
@app.route('/create_bucket')
def create_bucket_page():
    return render_template("create_bucket.html")
    
""" we handle goal operations """
    
@app.route('/goals')
def view_goals():
    return render_template("goals.html")
    
@app.route('/create_goal')
def create_goals():
    return render_template("create_goal.html")