from flask import Flask, render_template, redirect, request, session, flash
import re
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
    errorCount = 0
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        errorCount += 1
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address!")
        errorCount += 1
    if len(request.form['fName']) < 1:
        flash("First Name cannot be blank!")
        errorCount += 1
    if len(request.form['lName']) < 1:
        flash("Last Name cannot be blank!")
        errorCount += 1
    if len(request.form['password']) < 1:
        flash("Password cannot be blank!")
        errorCount += 1
    elif len(request.form['password']) <= 8:
        flash("Password must be longer than 8 characters!")
        errorCount += 1
    else:
        if request.form['password'] == request.form['password'].lower():
            flash("Password must contain at least one uppercase letter!")
            errorCount += 1
        if request.form['password'].isalpha():
            flash("Password must contain at least one number!")
            errorCount += 1
    if len(request.form['passwordConfirm']) < 1:
        flash("Confirm Password field cannot be blank!")
        errorCount += 1
    if request.form['password'] != request.form['passwordConfirm']:
        flash("Passwords must match!")
        errorCount += 1
    date = request.form['birthdate']
    curr = datetime.datetime.now().strftime("%Y-%m-%d")
    datetime.datetime.strptime(date, '%Y-%m-%d')
    date = date.split("-")
    curr = curr.split("-")
    if int(date[0]) > int(curr[0]) or int(date[2]) > 31 or int(date[2]) < 1 or int(date[1]) < 1 or int(date[1]) > 12:
        #general failure cases - year is in the future, or month/dates are impossible regardless of month or year
        flash("Invalid birthdate!")
    elif date[0] == curr[0]: #date is in current year (would ordinarily fail anyway as user would be too young)
        if int(date[1]) > int(curr[1]):
            flash("Invalid birthdate1")
        elif date[1] == curr[1]:
            if int(date[2]) > int(curr[2]):
                flash("Invalid birthdate!")
    else:
        #specific date checks - date can occur in given month, february 29th is legal only in leap years, etc.
        if date[1] == 2:
            if date[2] == 29 and not(date[1] % 4 == 0 and date[1] % 100 != 0 or date[1] % 400 == 0):
                flash("Invalid birthdate - February 29 does not occur in the given year!")
            elif int(date[2]) > 28:
                flash("Invalid birthdate!")
        elif int(date[1]) in [4,6,9,11]:
            if int(date[1]) > 30:
                flash("Invalid birthdate!")
    if errorCount > 0:
        session["success"] = False
    else:
        session["success"] = True
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)
