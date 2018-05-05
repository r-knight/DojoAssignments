from flask import Flask, render_template, redirect, request

app = Flask(__name__)        

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result', methods=['POST'])
def result():
	name = request.form["name"]
	fun = request.form["fun"]
	comment = request.form["comment"]
	return render_template('result.html', userFName = name, userFun = fun, userComment = comment)
@app.route('/danger')
def danger():
	print("User attempted to access /danger. User was redirected to root")
	return redirect('/')
if __name__=="__main__":
    app.run(debug=True) 