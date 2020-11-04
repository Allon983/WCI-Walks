import functools, sys

from flask import Blueprint, g, redirect, render_template, request, session, url_for
from models import database

bp = Blueprint('login', __name__, url_prefix='/users')

@bp.route('/', methods=('GET', 'POST', 'PUT', 'PATCH', 'DELETE'))
def login():
    if request.method == 'POST':      
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        print(username, file=sys.stderr)

        error = None
        db = database.get_db()

        if not username or not email or not password:
            error = "Please fill out all values."
        elif db.execute(
            "SELECT id FROM users WHERE email=?", (email,)
        ).fetchone() is None:
            error = "We couldn't find your account.\n\
            Please sign up if you haven't already."
        
        if error is None:
            #store a cookie
            print('Store a cookie', file=sys.stderr)

        #in the future, alert front end (maybe make an error html file?) for error

    return render_template('users.html')

@bp.route('/login', methods=('GET', 'POST', 'PUT', 'PATCH', 'DELETE'))
def filler():
    return render_template('users.html') #fix later

@bp.route('/sign-up', methods=('GET', 'POST'))
def signup():
    return render_template('users.html') #fix later