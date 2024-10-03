from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!, Here is another hello'

@app.route('/add/<x>/<y>')
def hi(x,y):
    added = x + y
    return '<h1>Here\'s a different message!<h1> <br/> The result of the addition is ' + str(added)
