from flask import Blueprint, render_template

from app.model.user import User

from app import my_db

bp = Blueprint('user',__name__,url_prefix='/user')

@bp.route('/')
def index():
    return render_template('user/index.html')
