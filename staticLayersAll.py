from flask import Flask #don't forget localhost:5000
app = Flask(__name__) #

@app.route('/')
def index():
    return "Hello World "

@app.route('/names/myname')
def hector():
    return "<h1>H E C T O R !!</h1>"

@app.route('/hello')
def hello():
    return "Hello"

@app.route('/nombre/minombre')
def manuel():
    return "Manuel"

@app.route('/echo/<message>')
def echo(msg):
    return 'your message was: ' + msg

if __name__ == "__main__":
	app.run()
