from flask import Flask
app = Flask(__name__) #

@app.route('/names/myname')
def hector():
    return "H E C T O R"

@app.route('/hello')
def index():
    return "Hello"  

if __name__ == "__main__":
	app.run()
