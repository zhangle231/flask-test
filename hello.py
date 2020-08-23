from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for

from flask_sqlalchemy import SQLAlchemy

#from tasks1 import add_together

app = Flask(__name__)
app.secret_key = 'some_secret'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)

from . import photo
app.register_blueprint(photo.bp)
#app.add_url_rule('/',endpoint='index')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, unique=False, nullable=False)
    bill_type = db.Column(db.String, unique=False, nullable=False)
    money = db.Column(db.String, unique=False, nullable=False)
    remark = db.Column(db.String, unique=False, nullable=False)

#db.drop_all()
#db.create_all() 

@app.route('/')
def hello_world():
    try:
        #result = add_together.delay(23,52)
        bills = Bill.query.all()
        app.logger.info('list')
        return render_template('test.html',bills=bills)
        #return 'Hello, World!' + str(result.wait())

    except Exception as e:
        print(e)
    return 'Hello, World!'

@app.route('/add')
def add():
    flash('You were successfully logged in')
    return render_template('add.html')
 
@app.route('/save')
def save():
    date = request.args.get('date', '')
    bill_type = request.args.get('type', '')
    money = request.args.get('money', '')
    remark = request.args.get('remark', '')
    #db.session.add(User(username="Flask1", email="example2@example.com"))
    db.session.add(Bill(date=date, bill_type=bill_type, money=money, remark=remark))
    db.session.commit()
    users = User.query.all()
    print(users)
    return redirect('/')

@app.route('/del')
def myDel():
    id = request.args.get('id','')
    bill = Bill.query.get(id)
    db.session.delete(bill)
    db.session.commit()
    return redirect('/')


