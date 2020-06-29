from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from movie import db
from movie.model.movie_model import Movie

bp = Blueprint('movie', __name__, url_prefix='/movie')

@bp.route('/')
def index():
    page = int(request.args.get('page', '1'))
    pagination = Movie.query.order_by(Movie.id.desc()).paginate(page,per_page=12,error_out=False)
    movies = pagination.items
    return render_template('movie/index.html', movies = movies, pagination=pagination)

@bp.route('/add', methods=('GET', 'POST'))
def add():
    if request.method ==  'POST':
        name = request.form['movieName']
        img_url = request.form['imgURL']
        flash('添加成功! ' + name)
        movie = Movie()
        movie.name = name
        movie.img_url = img_url
        db.session.add(movie)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('movie/add.html')
