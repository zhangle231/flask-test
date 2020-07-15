from flask import Blueprint, render_template, request, redirect, url_for

from app import my_db

from app.model.menu import Menu

import datetime

bp = Blueprint('menu',__name__,url_prefix='/menu')

'''
menus = {'name':'1 test','is_leaf':0,
           'children':[
                    {'name':'1.1 test','is_leaf':1,'children':None},
                    {'name':'1.2 test','is_leaf':0,
                     'children':[
                            {'name':'1.2.1 test','is_leaf':0,'children':[
                                    {'name':'1.2.1.1 test','is_leaf':0,'children':[
                                        {'name':'1.2.1.1.1 test','is_leaf':0,'children':[
                                            {'name':'1.1 test','is_leaf':1,'children':None},
                                        ]},
                                    ]},
                            ]}
                        ]}
            ]
          }
 
'''
def reuse(pid,l,r):
    l = [ e for e in l if e not in r]
    if len(l) == 0:
        return r
    for e in l:
        if e.pid == pid:
            r.append(e)
            r = reuse(e.id,l,r)
    return r

def get_menu(menus):
    r = []
    res = reuse(0,menus,r)
    return res

def create_menu():
    menus = Menu.query.all()
    menus = sorted(menus, key=lambda x:x.id)
    menus = get_menu(menus)
    return menus

@bp.route('/')
def index():
    menus = create_menu()
    return render_template('menu/index.html', menus=menus)

@bp.route('/add', methods=('POST','GET'))
def add():
    if request.method == 'POST':
        menu = Menu()
        pname = request.form['pname'].strip()
        menu.name = request.form['name']
        menu.url = request.form['url']

        if pname == '':
            menu.pid = 0

        else:
            pmenu = Menu.query.filter(Menu.name == pname).first()
            menu.pid = pmenu.id

        my_db.session.add(menu)
        my_db.session.commit()

        return redirect(url_for('menu.index'))
    return render_template('menu/add.html')
