from flask import Flask, render_template

app = Flask(__name__)        

@app.route('/play')
def play():
    return render_template('index.html', num=3, col="blue")
@app.route('/play/<number>')
def play2(number):
    return render_template('index.html', num = int(number), col="blue")
@app.route('/play/<number>/<color>')
def index(number,color):
    return render_template('index.html', num=int(number), col = color)
if __name__=="__main__":
    app.run(debug=True) 