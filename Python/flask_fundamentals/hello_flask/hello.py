from flask import Flask, render_template, request

app = Flask(__name__)

print(__name__)         

@app.route('/')
def hello_world():
    return render_template('index.html', name="Ryan")
if __name__=="__main__":
    app.run(debug=True) 