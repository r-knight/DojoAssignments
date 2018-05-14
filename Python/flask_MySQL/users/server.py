from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
app.secret_key ="????????????????"
mysql = connectToMySQL('friendsdb')
r = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
def isValidEmail(email):
    if len(email) > 7:
        if re.match(r, email) != None:
            return True
    return False

@app.route('/')
def root():
    return redirect ('/users')
@app.route('/users')
def index():
    users_query = "SELECT * FROM FRIENDS"
    result = mysql.query_db(users_query)
    print(result)
    return render_template('/index.html', users=result)
@app.route('/users/new')
def new():
    return render_template('add_user.html')
@app.route('/users/<id>/edit')
def edit(id):
    user_query = "SELECT * FROM FRIENDS WHERE id=(%(id)s)"
    data ={
        'id': id
    }
    result = mysql.query_db(user_query, data)
    print(result)
    return render_template ('/edit_user.html', user = result[0])
@app.route('/users/<id>', methods=['GET'])
def show(id):
    user_query = "SELECT * FROM FRIENDS WHERE id=(%(id)s)"
    data ={
        'id': id
    }
    result = mysql.query_db(user_query, data)
    print(result)
    return render_template ('/view_user.html', user=result[0])
@app.route('/users/create', methods=['POST'])
def create():
    errorCount = 0
    session['f_name'] = request.form['f_name']
    session['l_name'] = request.form['l_name']
    session['email'] = request.form['email']

    if session['email'] !="":
        email_query = "SELECT * FROM friends WHERE email = %(email)s;"
        data = { 'email' : session['email'] }
        result = mysql.query_db(email_query, data)
        if not isValidEmail(data['email']):
            errorCount +=1
            flash("Invalid email adress")
        elif result != ():
            errorCount +=1
            flash("Email already registered!")
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
            'first_name': request.form['f_name'],
            'last_name': request.form['l_name'],
            'email': request.form['email']
        }
        query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        result = mysql.query_db(query, data)
        return redirect ("/users/"+ str(result)+ "")
    else:
        return redirect ("/users/new")
    return redirect ('/users')
@app.route('/users/<id>/destroy')
def destroy(id):
    data = {'id': id}
    query = "DELETE FROM friends WHERE id = %(id)s"
    mysql.query_db(query, data)
    print ("Deleted user with id: " + id)
    return redirect ('/users')
@app.route('/users/<id>', methods=['POST'])
def update(id):
    #Verify user inputs, send update query if all fields are valid, else redirect to edit page with flash messages
    errorCount = 0
    f_name = request.form['f_name']
    l_name = request.form['l_name']
    email = request.form['email']
    update_email = True #There will be cases where it's desirable to not change email

    if email !="":
        email_query = "SELECT * FROM friends WHERE email = %(email)s;"
        data = { 'email' : email }
        result = mysql.query_db(email_query, data)
        if not isValidEmail(data['email']):
            errorCount +=1
            flash("Invalid email adress")
        elif result != ():
            if int(result[0]['id']) == int(id):
                update_email = False #Cur3rent user has this address currently. No need to update
            else:
                errorCount +=1
                flash("Email already registered!")
    else:
        errorCount +=1
        flash("Email field must not be blank")
  
    if f_name != "":
        if len(f_name) < 2:
            errorCount +=1
            flash("First name must be at least 2 characters!")
        elif not f_name.isalpha():
            errorCount +=1
            flash("First name must contain only letters!")
    else:
        errorCount +=1
        flash("First name field must not be blank!")
    if l_name != "":
        if len(l_name) < 2:
            errorCount +=1
            flash("Last name must be at least 2 characters!")
        elif not l_name.isalpha():
            errorCount +=1
            flash("Last name must contain only letters!")
    else:
        errorCount +=1
        flash("Last name field must not be blank!")

    if errorCount == 0:
        data = {
            'first_name': request.form['f_name'],
            'last_name': request.form['l_name'],
            'email': request.form['email'],
            'id':id
        }
        if update_email:
            query = "UPDATE friends SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s "
        else:
            query = "UPDATE friends SET first_name = %(first_name)s, last_name = %(last_name)s, updated_at = NOW() WHERE id = %(id)s "
        result = mysql.query_db(query, data)
        return redirect ("/users/"+ str(data['id'])+ "")
    else:
        data = {
            'id': id
        }
        return redirect ("/users/"+ str(data['id'])+ "/edit")

if __name__ == '__main__':
    app.run(debug=True)