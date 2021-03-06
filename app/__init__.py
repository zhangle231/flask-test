import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

my_db = SQLAlchemy()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'my_db.sqlite'),
        UPLOAD_FOLDER = os.path.join(app.instance_path, 'upload'),
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.instance_path, 'test.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True,
    )
  
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
  
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # config db
    my_db.init_app(app)
   
    # a simple page that says hello
    @app.route('/hello')
    def hello():
      return 'Hello, World!'
  
    from . import db
    db.init_app(app)
  
    # 权限管理
    from . import auth
    app.register_blueprint(auth.bp)
  
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    # 用户管理
    from . import user
    app.register_blueprint(user.bp)

    # Role
    from . import role
    app.register_blueprint(role.bp)

    # 菜单管理
    from . import menus
    app.register_blueprint(menus.bp)
 
    # 项目管理
    from . import project_manager
    app.register_blueprint(project_manager.bp)

    # weight
    from . import weight
    app.register_blueprint(weight.bp)

    # movie
    from . import movie
    app.register_blueprint(movie.bp)
  
    return app
