from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'PotatoesBoilEmMashEmStickEmInAStew12536134'

@app.route('/')
def index():
	if 'counter' in session:
		session['counter'] +=1
	else:
		session['counter'] = 1
	return render_template("index.html")
	
@app.route('/destroy_session')
def destroy():
	session.clear()
	return redirect('/')
@app.route('/increment', methods=['POST'])
def show_user():
	session['counter'] +=1
	return redirect ('/')
@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect ('/')

if __name__=="__main__":
    app.run(debug=True) 
