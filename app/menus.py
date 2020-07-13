from flask import Blueprint, render_template, request, redirect, url_for

from app import my_db

import datetime

bp = Blueprint('menu',__name__,url_prefix='/menu')

@bp.route('/')
def index():
    return render_template('menu/index.html')


