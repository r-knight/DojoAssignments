from flask import Flask, render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
app.secret_key ="okayImReallyGettingSickOfWritingTheseKeysEveryTime"
bcrypt = Bcrypt(app)
mysql = connectToMySQL('login_regv1db')
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
    errorCount = 0
    session['f_name'] = request.form['f_name']  
    session['l_name'] = request.form['l_name']
    session['email'] = request.form['email']   
    if request.form['password'] != "":
        if len(request.form['password']) < 8:
            errorCount +=1
            flash("Password must be at least 8 characters!")
            pw_hash = None
        elif request.form['password'].isalpha():
            errorCount +=1
            flash("Password must contain at least one number or special character")
            pw_hash = None
        else:
            pw_hash = bcrypt.generate_password_hash(request.form['password'])
        if request.form['passwordConfirm'] !="":
            if not bcrypt.check_password_hash(pw_hash, request.form['passwordConfirm']):
                errorCount +=1
                flash("Password and Password Confirmation fields must match")
        else:
            errorCount +=1
            flash("Password confirmation field must not be blank!")
    else:
        errorCount +=1
        flash("Password field must not be blank")
    if request.form['email'] !="":
        email_query = "SELECT * FROM users WHERE email = %(email)s;"
        data = { 'email' : request.form['email'] }
        session['email'] = data['email']
        result = mysql.query_db(email_query, data)
        if not isValidEmail(data['email']):
            errorCount +=1
            flash("Invalid email adress")
        elif result != ():
            errorCount +=1
            flash("Email already registered")
    else:
        errorCount +=1
        flash("Email field must not be blank")
  
    if session['f_name'] != "":
        if len(session['f_name']) < 2:
            errorCount +=1
            flash("First name must be at least 2 characters!")
        elif not session['f_name'].isalpha():
            errorCount +=1
            flash("First name must contain only letters!")
    else:
        errorCount +=1
        flash("First name field must not be blank!")
    if session['l_name'] != "":
        if len(session['l_name']) < 2:
            errorCount +=1
            flash("Last name must be at least 2 characters!")
        elif not session['l_name'].isalpha():
            errorCount +=1
            flash("Last name must contain only letters!")
    else:
        errorCount +=1
        flash("Last name field must not be blank!")
    if errorCount == 0:
        data = {
            'email': session['email'],
            'f_name': session['f_name'],
            'l_name': session['l_name'],
            'pw_hash': pw_hash
        }
        session.clear()        
        query = "INSERT INTO users (f_name, l_name, email, pw_hash, created_at, updated_at) VALUES (%(f_name)s, %(l_name)s, %(email)s, %(pw_hash)s, NOW(), NOW());"
        session['id'] = mysql.query_db(query, data)
        flash("Thank you for registering!")
        return redirect('/success')
    else:
        flash(str(errorCount) + " error(s) occurred. Please read the error messages and try again")
        return redirect('/')
@app.route('/success')
def success(): 
    data ={
        'id': str(session['id'])
    }
    name_query = "SELECT f_name FROM users WHERE id=(%(id)s)"
    name = mysql.query_db(name_query, data)
    name = name[0]['f_name']
    return render_template('/success.html', u_name=name)
@app.route('/login', methods=['POST'])
def login(): 
    email_query = "SELECT * FROM users WHERE email = %(email)s;"
    data={'email':request.form['e_email']}
    result = mysql.query_db(email_query, data)
    print(result)
    if result != ():
        if bcrypt.check_password_hash(result[0]['pw_hash'], request.form['e_password']):
            session['id'] = result[0]['id']
            return redirect('/success')
    else:
        flash("Invalid credentials")
        return redirect ('/')
@app.route('/logout', methods=['POST'])
def logout(): 
    session.clear()
    return redirect ('/')
if __name__ == '__main__':
    app.run(debug=True)