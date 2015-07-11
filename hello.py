from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route("/")
def index():
    response = make_response('<h1>This doucment carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response
#    user_agent = request.headers.get('User-Agent')
#    return '<p>Your browser is %s</p>' % user_agent

@app.route("/user/<name>")
def user(name):
    return '<h1>hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)