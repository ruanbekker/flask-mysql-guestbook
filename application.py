from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy # instantiate database object # import class
from os import environ

MYSQL_USER=environ['MYSQL_USER']
MYSQL_PASSWORD=environ['MYSQL_PASSWORD']
MYSQL_HOST=environ['MYSQL_HOST']
MYSQL_DATABASE=environ['MYSQL_DATABASE']

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{user}:{passwd}@{host}/{db}'.format(user=MYSQL_USER, passwd=MYSQL_PASSWORD, host=MYSQL_HOST, db=MYSQL_DATABASE)
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application) # instantiate database object #interface with flask app itself

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(1000))

@application.route('/')
def index():
    result = Comments.query.all() # use the comments class
    #result = Comments.query.filter_by(name='Ruan')
    counts = Comments.query.count()
    return render_template('index.html', result=result, counts=counts)

@application.route('/sign')
def sign():
    return render_template('sign.html')

@application.route('/search')
def search():
    return render_template('search.html')


@application.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']

    signature = Comments(name=name, comment=comment)      # instantiate an object. signature object, from comments class
    db.session.add(signature)                 # add a row to database
    db.session.commit()                     # save changes

    return redirect(url_for('index'))
    return render_template('index.html', name=name, comment=comment)

@application.route('/searchresults', methods=['GET', 'POST'])
def searchresults():
    name = request.form['name']
    result = Comments.query.filter_by(name=name)
    counts = result.count()
    return render_template('index.html', result=result, counts=counts)

if __name__ == '__main__':
    db.create_all()
    application.run(host="0.0.0.0")
