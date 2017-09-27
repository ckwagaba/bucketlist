# import required modules

from flask import render_template, redirect, url_for, request, session
from app import app
from functionality.user import *
from functionality.buckets import *
from functionality.goals import *

# global var. reset when server is restarted
all_users = []

# set the secret key.  for sessions:
app.secret_key = 'DqvjteLU#m@k2S'

""" landing page - which happens to also be the sign in page """

@app.route('/')
def index():
    if 'user' in session:
        return render_template("buckets.html", user = session['user'])
    else:
        return render_template("sign_in.html")

""" we handle user registration """

@app.route('/register')
def signup_page():
    if 'user' in session:
        return render_template("buckets.html", user = session['user'])
    else:
        return render_template("register.html")
    
@app.route('/register', methods = ['POST', 'GET'])
def create_user():
    if request.method == 'POST': # proper form submission
        # get values from request
        name = request.form['user_name']
        email = request.form['user_email']
        password = request.form['user_password']
        # we need to check if the user exists
        for user in all_users:
            if user['email'] == email:
                error = 'User already exists'
                return render_template("register.html", error = error)
        else: # update global user object with values
            new_user = User(name, email, password, [])
            this_user = new_user.create_user()
            all_users.append(this_user)
            # then redirect to sign in
            return redirect('/signin')
    else: # show registration form
        return redirect('/register')
    
""" we handle user login and logout """

@app.route('/signin')
def signin_page():
    if 'user' in session:
        return render_template("buckets.html", user = session['user'])
    else:
        return render_template("sign_in.html")
    
@app.route('/signin', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST': # proper form submission
        # get values from request
        email = request.form['user_email']
        password = request.form['user_password']
        # Authenticate user
        for user in all_users:
            if user['email'] == email and user['password'] == password:
                # set session variable using the user object
                session['user'] = user
                return redirect('/buckets')
        error = 'Verify your credentials and try again'
        return render_template("sign_in.html", error = error)
    else: # show login form
        return redirect('/signin')
        
@app.route('/logout')
def logout():
    # destroy this user's session
    session.pop('user', None)
    return redirect(url_for('index'))
    
""" we handle bucket operations """

@app.route('/buckets')
def view_buckets():
    # protect route from unauthorized users
    if 'user' in session:
        return render_template("buckets.html", user = session['user'])
    else:
        return redirect(url_for('index'))

@app.route('/create_bucket')
def create_bucket_page():
    if 'user' in session:
        return render_template("create_bucket.html", user = session['user'])
    else:
        return redirect(url_for('index'))
    
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
    if 'user' in session:
        return render_template("goals.html", user = session['user'])
    else:
        return redirect(url_for('index'))
    
@app.route('/create_goal')
def create_goals_page():
    if 'user' in session:
        return render_template("create_goal.html", user = session['user'])
    else:
        return redirect(url_for('index'))
    
@app.route('/create_goal', methods = ['POST', 'GET'])
def create_goals():
    return 'Still to handle this and more. But the functionality and tests for it exist. Thanks.'