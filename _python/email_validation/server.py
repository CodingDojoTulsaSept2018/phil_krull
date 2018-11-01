from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import connectToMySQL

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'My super secret key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emails', methods=['post'])
def create():
    if len(request.form['email']) < 1:
        flash('Please enter a email address')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Please enter a valid email address')
    else:
        mysql = connectToDb()

        query = 'INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());'
        data = { 'email': request.form['email']}
        mysql.query_db(query, data)
        email = request.form['email']
        flash(f'The email you entered: { email }, is a Valid Email.  Thank you!')
        return redirect('/success')
    return redirect('/')

@app.route('/success')
def success():
    mysql = connectToDb()
    allEmails = mysql.query_db('SELECT id, email, DATE_FORMAT(created_at, "%c/%d/%y %h:%i:%s %p") AS made FROM emails;')

    return render_template('success.html', emails = allEmails)

@app.route('/emails/<id>')
def destroy(id):
    mysql = connectToDb()
    query = 'SELECT email FROM emails WHERE id = %(id)s;'
    data = { 'id':id }
    email = mysql.query_db(query, data)
    flash(f"{ email[0]['email'] } successfull deleted")

    mysql = connectToDb()
    query = 'DELETE FROM emails WHERE id = %(id)s;'
    data = { 'id':id }
    mysql.query_db(query, data)

    return redirect('/')

def connectToDb():
    return connectToMySQL('emails')

if __name__ == "__main__":
    app.run(debug=True)
