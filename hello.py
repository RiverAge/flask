from flask import Flask, render_template, session, url_for, flash
from flask import request
from flask import make_response
from flask import redirect
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)

#basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#app.config['SQLALCHEMY_DATATABASE_URI'] = 'sqlite_dir'
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name') 
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
#        form.name.data = ''
    return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())
#    return render_template('index.html', current_time=datetime.utcnow())

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

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'the about page', 300

@app.route('/test-form/', methods=['get', 'post'])
def form():
#    return 'i am test form'
#    return request.headers.get('User-Agent')
    return request.form.get('password')

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')  
    
    def __repr__(self):
        return '<Role %r>' % self.name
    
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr_(self):
        return '<User %>' % self.username
class NameForm(Form):
    name = StringField('What is your name', validators=[Required()])
    submit = SubmitField('Submit')
if __name__ == '__main__':
#    app.run()
    manager.run()