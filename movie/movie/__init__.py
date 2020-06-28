from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

    return app

