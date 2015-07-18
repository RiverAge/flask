from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import redirect
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)

@app.route("/")
def index():
    return render_template('index.html', current_time=datetime.utcnow())
#    response = make_response('<h1>This doucment carries a cookie!</h1>')
#    response.set_cookie('answer', '42')
#    return render_template('index.html')
#    return response
#    user_agent = request.headers.get('User-Agent')
#    return '<p>Your browser is %s</p>' % user_agent

@app.route("/user/<name>")
def user(name):
    return render_template('user.html', name = name)
#    return '<h1>hello, %s!</h1>' % name

@app.route("/redi")
def redi():
    return redirect('http://jwss.cc')


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



if __name__ == '__main__':
#    app.run()
    manager.run()