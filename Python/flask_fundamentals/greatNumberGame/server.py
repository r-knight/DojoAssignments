from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'PotatoesBoilEmMashEmStickEmInAStew1829364'

@app.route('/')
def index():
	if 'number' not in session:
		session['number'] = random.randrange(1, 101)
	return render_template("index.html")
	
@app.route('/destroy_session')
def destroy():
	session.clear()
	return redirect('/')
@app.route('/submit', methods=['POST'])
def submit():
	session['guess'] = request.form['guess']
	session['resultStr'] = ""
	if session['guess'] =="":
		session['guess'] = 0
	if int(session['guess']) == session['number']:
		session['resultStr'] += str(session['guess']) + " was the number!"
		session['color'] = "green"
		session['gameWon'] = True
	elif int(session['guess']) > session['number']:
		session['resultStr'] += "Too high!"
		session['color'] = "red"
	elif int(session['guess']) < session['number']:
		session['resultStr'] += "Too low!"
		session['color'] = "red"
		
	return redirect ('/')
@app.route('/reset', methods=['POST'])
def reset():
	session.pop('number')
	session.pop('guess')
	session.pop('color')
	session.pop('gameWon')
	return redirect ('/')

if __name__=="__main__":
    app.run(debug=True) 
