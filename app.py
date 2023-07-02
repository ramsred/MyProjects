from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def default_route():
    return "<h1> hello welcome to the show</h1>"

@app.route('/error')
def error_route():
    return "<h2> error page</h2>"

if __name__ == "__main__":
    app.run(port=8000)