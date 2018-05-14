from flask import Flask, render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
app.secret_key ="okayImReallyGettingSickOfWritingTheseKeysEveryTime"
bcrypt = Bcrypt(app)
mysql = connectToMySQL('walldb')
r = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
def isValidEmail(email):
    if len(email) > 7:
        if re.match(r, email) != None:
            return True
    return False

@app.route('/')
def index():    
    if 'id' in session:
        return redirect('/wall')    #redirect users to the Wall if they are already logged in
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
            if request.form['password_confirm'] !="":
                if not bcrypt.check_password_hash(pw_hash, request.form['password_confirm']):
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
    return redirect('/wall')
@app.route('/login', methods=['POST'])
def login(): 
    email_query = "SELECT * FROM users WHERE email = %(email)s;"
    data={'email':request.form['login_email']}
    result = mysql.query_db(email_query, data)
    print(result)
    if result != ():
        if bcrypt.check_password_hash(result[0]['pw_hash'], request.form['login_pw']):
            session['id'] = result[0]['id']
            return redirect('/success')
    else:
        flash("Invalid credentials")
        return redirect ('/')
@app.route('/wall')
def wall(): 
    if 'id' in session:
        print("Found ID! ID: ", session['id']) 
        data ={
            'id': str(session['id'])
        }
        #wall_query = "SELECT messages.id as POST_NUMBER, messages.message, messages.created_at, messages.updated_at, users.f_name AS MESSAGE_USER_F_NAME, users.l_name AS MESSAGE_USER_L_NAME, comments.user_id, comments.message_id, comments.comment, comments.created_at from messages LEFT JOIN users ON messages.user_id = users.id LEFT JOIN comments ON comments.message_id = messages.id ORDER BY messages.created_at desc, comments.created_at asc;"
        wall_query = "SELECT messages.id as POST_NUMBER, messages.message, messages.created_at as MESSAGE_CREATED_AT, messages.updated_at MESSAGE_UPDATED_AT, original_poster.f_name AS MESSAGE_USER_F_NAME, original_poster.l_name AS MESSAGE_USER_L_NAME, commentor.f_name AS COMMENTOR_F_NAME, commentor.l_name AS COMMENTOR_L_NAME, comments.user_id, comments.message_id, comments.comment, comments.created_at as COMMENT_CREATED_AT, comments.updated_at as COMMENT_UPDATED_AT from messages LEFT JOIN users AS original_poster ON messages.user_id = original_poster.id LEFT JOIN comments ON comments.message_id = messages.id LEFT JOIN users AS commentor ON commentor.id = comments.user_id ORDER BY messages.created_at desc, comments.created_at asc;"
        wall_messages = mysql.query_db(wall_query)
        name_query = "SELECT f_name FROM users WHERE id=(%(id)s)"
        name = mysql.query_db(name_query, data)
        name = name[0]['f_name']
        return render_template('/wall.html', uid=session['id'], content=wall_messages, u_name = name)
    else:
        flash("You must be logged in to view that page!")
        return redirect('/')
@app.route('/post_message', methods=['POST'])
def post_message():
    user_message = request.form['new_message']
    if(user_message) != "" and 'id' in session:
        data = {
            'id': str(session['id']),
            'message': user_message 
        }
        message_query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (%(id)s, %(message)s, NOW(), NOW());"
        mysql.query_db(message_query, data)
    return redirect('/wall')
@app.route('/post_comment', methods=['POST'])
def post_comment():
    user_comment = request.form['new_comment']
    if(user_comment) != "" and 'id' in session:
        data = {
            'user_id': str(session['id']),
            'comment': user_comment,
            'message_id': request.form['post_id']
        }
        comment_query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (%(user_id)s, %(message_id)s, %(comment)s, NOW(), NOW());"
        mysql.query_db(comment_query, data)
    return redirect('/wall')
@app.route('/logout')
def logout(): 
    session.clear()
    return redirect ('/')
if __name__ == '__main__':
    app.run(debug=True)