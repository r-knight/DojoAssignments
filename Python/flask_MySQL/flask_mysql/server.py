from flask import Flask
from flask_bcrypt import Bcrypt
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
_app = Flask(__name__)
bcrypt = Bcrypt(_app)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('mydb')
# now, we may invoke the query_db method
print('all the users', mysql.query_db("select * from users;"))
if __name__ == '__main__':
    _app.run(debug=True)