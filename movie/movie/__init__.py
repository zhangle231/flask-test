from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import click
from flask.cli import with_appcontext

import json


db = SQLAlchemy()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    from movie.model.movie_model import Movie
    f = open('/home/leo/project/flask-test/movie/scrapy/movie_scrapy/test.json')
    buff = f.read()
    objs = json.loads(buff)
    for obj in objs:
        movie = Movie()
        movie.name = obj['text']
        movie.img_url = obj['img']
        db.session.add(movie)
        db.session.commit()
    click.echo('Initialized the database.')

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    )

    db.init_app(app)

    from . import movie

    app.register_blueprint(movie.bp)
    app.add_url_rule('/movie/', endpoint='index')

    app.cli.add_command(init_db_command)

    return app

