from flask import Flask, render_template, redirect, request,flash
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
app.secret_key = "Originalsecretkeydonutsteel!"
mysql = connectToMySQL('emailvalidationdb')
r = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
def isValidEmail(email):
    if len(email) > 7:
        if re.match(r, email) != None:
            return True
    return False

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/create_user', methods=['POST'])
def create():
    data = {
         'email': request.form['email']
       }
    if isValidEmail(data["email"]):
        query = "INSERT INTO users (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"

        mysql.query_db(query, data)
        flash("Email " + data['email'] +" is valid! Thank you for registering!")
        return redirect('/success')
    else:
        flash("Invalid email. Please try again")
        return redirect('/')
@app.route('/success')
def success():
    all_users = mysql.query_db("SELECT * FROM users")
    print (all_users)
    return render_template('success.html', users=all_users)
if __name__ == '__main__':
    app.run(debug=True)