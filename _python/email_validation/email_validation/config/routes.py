from email_validation import app
from email_validation.controllers.emails import Emails
email = Emails()

@app.route('/')
def index():
    return email.index()

@app.route('/emails', methods=['post'])
def create():
    return email.create()

@app.route('/success')
def success():
    return email.success()

@app.route('/emails/<id>')
def destroy(id):
    return email.destroy(id)