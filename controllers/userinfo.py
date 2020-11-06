import functools, sys

from flask import Blueprint, redirect, render_template, request
from models import database

bp = Blueprint('login', __name__, url_prefix='/users')

@bp.route('/', methods=('GET', 'POST', 'PUT', 'PATCH', 'DELETE'))
def info():
    #check for cookie
    #if no cookie redirect to login
    return render_template('users.html') #fix later

@bp.route('/signup', methods=('GET', 'POST', 'PUT', 'PATCH', 'DELETE'))
def signup():
    if request.method == 'POST':      
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        print(username, file=sys.stderr)

        error = None
        db = database.get_db()

        if not username or not email or not password:
            error = 'Please fill out all values.'
        elif db.execute(
                'SELECT id FROM users WHERE email=?', (email,)
            ).fetchone() is not None:
                error = 'This email is already taken.'
        
        if error is None:
            # implement two factor auth
            #encrypt password later
            db.execute(
                'INSERT INTO users (email, username, password, distance) VALUES (?, ?, ?, 0)', (email, username, password)
            )
            db.commit()
            return redirect('/users/login')

        #in the future, alert front end of error with http response
        print(error, file=sys.stderr)

    return render_template('usersignup.html') #fix later

@bp.route('/login', methods=('GET', 'POST', 'PUT', 'PATCH', 'DELETE'))
def login():
    if request.method == 'POST':      
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        print(username, file=sys.stderr)

        error = None
        db = database.get_db()

        if not username or not email or not password:
            error = 'Please fill out all values.'
        else:
            user = db.execute(
                'SELECT id FROM users WHERE email=?', (email,)
            ).fetchone()
            if user is None:
                error = 'Username not found. Have you signed up yet?'
            elif password != user['password']:
                error = 'Incorrect password.'
        
        if error is None:
            #store a cookie
            print('Store a cookie', file=sys.stderr)
            return redirect('/users')

        #in the future, alert front end of error with http response
        print(error, file=sys.stderr)

    return render_template('userlogin.html')