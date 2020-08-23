from flask import Blueprint, render_template, request, redirect, url_for

from app import my_db

from app.model.menu import Menu

from .common import reuse, get_menu, create_tree

import datetime

bp = Blueprint('menu', __name__, url_prefix='/menu')

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

def create_menu():
    '''获取菜单树，获取数据库信息，并生成数据结构
    '''
    menus = Menu.query.all()
    menus = sorted(menus, key=lambda x: x.id)
    menus = get_menu(menus)
    return menus

def create_treemenu():
    data = Menu.query.all()
    ret = {'id': 1, 'pid': 0, 'is_leaf': 1,
           'name': data[0].name, 'children': []}
    create_tree(1, data, ret)
    return ret


@bp.route('/')
def index():
    menus = create_menu()

    tree = create_treemenu()
    return render_template('menu/index.html', menus=menus, tree=tree)


@bp.route('/add', methods=('POST', 'GET'))
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
