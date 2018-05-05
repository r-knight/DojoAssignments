from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key = 'PotatoesBoilEmMashEmStickEmInAStew1829364'

@app.route('/')
def index():
	if 'gold' not in session:
		session['gold'] = 0
	if 'activities' not in session:
		session['activities'] = [] # list that will contain dictionaries
	return render_template("index.html")
@app.route('/process_money', methods=['POST'])
def process_money():
	gold = 0
	dgold = 0
	bldg = request.form["building"]
	time = datetime.datetime.utcnow()
	if bldg == "farm":
		dgold = random.randrange(10,21)
	elif bldg == "cave":
		dgold = random.randrange(5,11)
	elif bldg == "house":
		dgold = random.randrange(2,6)
	elif bldg == "casino":
		dgold = random.randrange(-50,51)
	
	gold += dgold 
	session['gold'] += gold
	activity = {'gold':abs(gold), 'location':bldg, 'timestamp':time, 'result':"won"}
	if dgold < 0:
		activity["result"] = "lost"
	session['activities'].append(activity)
	
	return redirect ('/')
@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect ('/')

if __name__=="__main__":
    app.run(debug=True) 
