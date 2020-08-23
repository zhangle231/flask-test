from flask import Blueprint, render_template, request, redirect, url_for

from app.model.user import User

from app import my_db

import datetime

bp = Blueprint('user',__name__,url_prefix='/user')

@bp.route('/', methods=('POST','GET'))
def index():
    if request.method == 'POST':
        username = request.form['username'].strip()
        phone = request.form['phone'].strip()
        query = User.query
        if username != "":
            query = query.filter(User.username == username)
        if phone != "":
            query = query.filter(User.phone == phone)

        users = query.all()
    else:
        users = User.query.all()
    return render_template('user/index.html', users=users)


@bp.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        user = User()
        user.username    = request.form['username']
        user.password    = request.form['password']         
        user.dep         = request.form['dep']             
        user.phone       = request.form['phone']         
        user.mail        = request.form['mail']         
        user.status      = request.form['status']         
        user.post        = request.form['post']    
        user.remarks     = request.form['remarks']         
        user.create_time = datetime.datetime.now()

        my_db.session.add(user)
        my_db.session.commit()

        return redirect(url_for('user.index'))
    else:
        return render_template('user/add.html')

@bp.route('/<int:id>/update', methods=('GET','POST'))
def update(id):
    user = User.query.get(id)
    if request.method == 'POST':
        user.username    = request.form['username']
        user.password    = request.form['password']         
        user.dep         = request.form['dep']             
        user.phone       = request.form['phone']         
        user.mail        = request.form['mail']         
        user.status      = request.form['status']         
        user.post        = request.form['post']    
        user.remarks     = request.form['remarks']         
        user.create_time = datetime.datetime.now()

        my_db.session.add(user)
        my_db.session.commit()

        return redirect(url_for('user.index'))
    else:
        return render_template('user/update.html', user=user)

@bp.route('/<int:id>/delete', methods=('GET',))
def delete(id):
    user = User.query.get(id)
    my_db.session.delete(user)
    my_db.session.commit()
    return redirect(url_for('user.index'))


