from flask import Flask, render_template, request  
app = Flask(__name__) 

print(__name__)
@app.route('/')

def hello_world():
    return 'Hello World!'
	
@app.route('/dojo')
def dojo():
  return "Dojo!"
@app.route('/say/<name>')
def hello(name):
    print(name)
    return "Hi "+name.capitalize()+"!"
@app.route('/repeat/<number>/<string>')
def repeat(number, string):
    print(number)
    print(string)
    return string * int(number)
if __name__=="__main__":   
    app.run(debug=True)    
