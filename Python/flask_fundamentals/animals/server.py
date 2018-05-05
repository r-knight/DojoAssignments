from flask import Flask, render_template, request,redirect

app = Flask(__name__)

print(__name__)         

@app.route('/')
def index():
    return render_template('index.html', num=3)
@app.route('/<number>')
def index2(number):
	if int(number) > 10:
		return redirect('/danger')
	elif int(number)>=1:
		return render_template('index.html', num=int(number))
	else:
		return render_template('index.html', num=3)
@app.route('/danger')
def danger():
    return render_template('danger.html')
if __name__=="__main__":
    app.run(debug=True) 