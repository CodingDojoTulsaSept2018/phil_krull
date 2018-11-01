from flask import Flask, render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL


import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.secret_key = 'My super secret key'

@app.route('/')
def index():
    if 'user_id' in session:
        flash('already logged in')
        return redirect('/success')
    return render_template('index.html')

@app.route('/logout', methods=['post'])
def logout():
    # clear all keys from session
    mysql = connect_to_db()
    query = "SELECT * FROM users WHERE id = %(id)s AND email_hash = %(hashed_em)s"
    data = {
        'id': session['user_id'],
        'hashed_em': session['email_hash']
    }

    result = mysql.query_db(query, data)
    print('*'*90)
    print(result)
    if len(result) > 0:
        session.clear()
        flash('successfully logged out')
        return redirect('/')
    else:
        # someone is trying to hack the system
        flash('you computer will self destruct in 30 sec')
        return redirect('/success')

@app.route('/success')
def success():
    # session.clear()
    # checking if key is in session
    if 'user_id' not in session:
        flash('must be logged in to continue')
        return redirect('/')
    mysql = connect_to_db()
    # query = 'SELECT first_name FROM users WHERE id = %(user_id)s'
    
    # data = {'user_id': session['user_id']}
    # user = mysql.query_db(query, data)

    # session['user_id'] = 20

    return render_template('success.html')
    # return render_template('success.html', user_name = user[0]['first_name'])

@app.route('/register', methods=['post'])
def register():
    user = request.form
    # validate the user input
    # 1. First Name - letters only, at least 2 characters and that it was submitted
    if len(user['first_name']) < 1:
        flash('first name is required')
    elif len(user['first_name']) < 2:
        flash('first name must be at least 2 chars long')
    elif not user['first_name'].isalpha():
        flash('first name must be characters')
    # 2. Last Name - letters only, at least 2 characters and that it was submitted
    if len(user['last_name']) < 1:
        flash('last name is required')
    elif len(user['last_name']) < 2:
        flash('last name must be at least 2 chars long')
    elif not user['last_name'].isalpha():
        flash('last name must be characters')
    # 3. Email - valid Email format, does not already exist in the database, and that it was submitted
    if len(user['email']) < 1:
        flash('email is required')
    elif not re.match(EMAIL_REGEX, user['email']):
        flash('enter a valid email')
    # check if email exist in db
    query = "SELECT id FROM users WHERE email = %(email)s"
    data = {'email': user['email']}

    mysql = connect_to_db()
    result = mysql.query_db(query, data)

    if len(result) > 0:
        flash('email already exists')

    print('email search is: ', result)
    print('='*90)

    # 4. Password - at least 8 characters, and that it was submitted
    if len(user['password']) < 1:
        flash('password is required')
    elif len(user['password']) < 8:
        flash('password must be at least 8 chars long')
    # 5. Password Confirmation - matches password
    if not user['password'] == user['confirm_password']:
        flash('passwords must match')

    if '_flashes' in session.keys():
        # failed validations
        # display the errors
        # redirect to index
        return redirect('/')
    else:
        # hash the password
        hashed_pw = bcrypt.generate_password_hash(user['password'])
        # hash the eamil for security purposes
        hashed_em = bcrypt.generate_password_hash(user['email'])
        # save the user
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at, email_hash) VALUES (%(fn)s, %(ln)s, %(em)s, %(pw)s, NOW(), NOW(), %(em_hash)s)'
        data = {
            'fn': user['first_name'],
            'ln': user['last_name'],
            'em': user['email'],
            'pw': hashed_pw,
            'em_hash': hashed_em
        }
        mysql = connect_to_db()
        user_id = mysql.query_db(query, data)
        # save the user in session
        # setting a session key
        session['user_id'] = user_id
        session['email_hash'] = hashed_em

        print(result)
        # redirect to success
        return redirect('/success')

@app.route('/login', methods=['post'])
def login():
    user = request.form
    # check form data, to make sure its there
    if not user['email'] and not user['password']:
        flash('all fields are required')
        return redirect('/')
    # find user from form email
    query = "SELECT id, password, email_hash FROM users WHERE email = %(email)s"
    data = {'email': user['email']}

    mysql = connect_to_db()
    result = mysql.query_db(query, data)

    # if user
    if len(result) > 0:
        # check for matching passwords
        if bcrypt.check_password_hash(result[0]['password'], user['password']):
        # if passwords match
            # save user in session
            session['user_id'] = result[0]['id']
            session['email_hash'] = result[0]['email_hash']

            flash('thank you for logging in')
            # redirect ot success
            return redirect('/success')
        # else
        else:
            # email and passwords do not match
            flash('invalid login attempt')
            # redirect to index
            return redirect('/')
    # if not user
    else:
        # invalid email
        flash('invalid log in attempt')
        # redirect to index
        return redirect('/')

def connect_to_db():
    return connectToMySQL('flask_login_reg')

if __name__ == "__main__":
    app.run(debug=True)
