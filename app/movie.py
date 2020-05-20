from flask import Blueprint, render_template

bp = Blueprint('movie',__name__,url_prefix='/movie')

@bp.route('/')
def index():
    return render_template('movie/index.html')

@bp.route('/<int:id>/play')
def play(id):
    return render_template('movie/play.html',id=id)
