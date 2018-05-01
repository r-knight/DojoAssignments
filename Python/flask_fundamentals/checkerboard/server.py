from flask import Flask, render_template

app = Flask(__name__)        

@app.route('/')
def play():
    return render_template('index.html', rows=8, cols=8)
@app.route('/<x>/<y>')
def custom(x,y):
    return render_template('index.html', rows=int(x), cols=int(y))
if __name__=="__main__":
    app.run(debug=True) 