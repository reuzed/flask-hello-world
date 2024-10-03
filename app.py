from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!, Here is another hello'

@app.route('/hi')
def hello_world():
    return 'Here\'s a different message!'
