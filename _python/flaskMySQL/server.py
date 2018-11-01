from flask import Flask
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL

app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('mydb')
# now, we may invoke the query_db method
allUsers = mysql.query_db("select created_at, name from users;")
print(type(allUsers))
print(allUsers[0])
print(type(allUsers[0]))
print(allUsers[0]['name'])
if __name__ == "__main__":
    app.run(debug=True)
