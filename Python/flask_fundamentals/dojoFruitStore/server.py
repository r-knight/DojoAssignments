from flask import Flask, render_template, redirect, request

app = Flask(__name__)        

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/checkout', methods=['POST'])
def checkout():
	raspberries = request.form["raspberries"]
	strawberries = request.form["strawberries"]
	apples = request.form["apples"]
	name = request.form["name"]
	studentId = request.form["studentId"]
	items = [raspberries, apples, strawberries]
	total = 0
	for i in range (len(items)):
		if items[i] == "":
			items[i] = 0
		total += int(items[i])
	return render_template('checkout.html', raspberry = items[0], strawberry = items[2], apple = items[1], fName = name, stuId = studentId, purchased = total)
if __name__=="__main__":
    app.run(debug=True) 