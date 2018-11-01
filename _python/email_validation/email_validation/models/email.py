from email_validation.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def create(self, form_data):
        errors = []
        if len(form_data['email']) < 1:
            errors.append('Please enter a email address')
        elif not EMAIL_REGEX.match(form_data['email']):
            errors.append('Please enter a valid email address')
        else:
            mysql = self.connectToDb()

            query = 'INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());'
            data = { 'email': form_data['email']}

            mysql.query_db(query, data)
            email = form_data['email']

        if len(errors) > 0:
            return False, errors
        else:
            return True, email

    def success(self):
        mysql = self.connectToDb()
        allEmails = mysql.query_db('SELECT id, email, DATE_FORMAT(created_at, "%c/%d/%y %h:%i:%s %p") AS made FROM emails;')
        return allEmails

    def destroy(self, id):
        mysql = self.connectToDb()
        query = 'SELECT email FROM emails WHERE id = %(id)s;'
        data = { 'id':id }
        email = mysql.query_db(query, data)

        mysql = self.connectToDb()
        query = 'DELETE FROM emails WHERE id = %(id)s;'
        data = { 'id':id }
        mysql.query_db(query, data)

        return email[0]['email']

    def connectToDb(self):
        return connectToMySQL('emails')