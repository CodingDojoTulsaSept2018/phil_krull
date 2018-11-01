from flask import render_template, redirect, session, flash, request
from email_validation.models.email import Email

email = Email()

class Emails:
    def index(self):
        return render_template('index.html')

    def create(self):
        result = email.create(request.form)
        if result[0]:
            flash(f'The email you entered: { result[1] }, is a Valid Email.  Thank you!')
            return redirect('/success')
        else:
            for error in result[1]:
                flash(error)
            return redirect('/')

    def success(self):
        allEmails = email.success()
        return render_template('success.html', emails = allEmails)

    def destroy(self, id):
        result = email.destroy(id)
        flash(f"{ result } successfully deleted")
        return redirect('/')

