from flask import Flask, render_template, redirect, request, flash, session

app = Flask(__name__)        
app.secret_key = "ThisIsSecretish!"
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result_test', methods=['POST'])
def result():
    errorCount = 0
    if request.form["name"] != "":
        name = request.form["name"]
        session["name"] = request.form["name"]
    else:
        flash("Name cannot be blank!")
        errorCount += 1
    if request.form["comment"] != "":
        session["comment"] = request.form["comment"]
        if len(request.form["comment"]) > 120:
            flash("Comment cannot be more than 120 characters!")
            errorCount += 1
    else:
        flash("Comment cannot be blank!")
        errorCount += 1
    if request.form.get("fun"):
        session["fun"] = request.form["fun"]
    else:
        flash("You didn't answer the second question")
        errorCount += 1
    if errorCount > 0:
        return redirect('/')
		
    return redirect('/result')
@app.route('/result')
def result2():
    return render_template('result.html')
@app.route('/danger')
def danger():
    print("User attempted to access /danger. User was redirected to root")
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True) 