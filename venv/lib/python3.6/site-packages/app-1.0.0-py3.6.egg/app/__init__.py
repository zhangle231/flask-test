import os
from flask import Flask

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__, instance_relative_config=True)
  
  print(app.instance_path)
  
  app.config.from_mapping(
      SECRET_KEY='dev',
      DATABASE=os.path.join(app.instance_path, 'my_db.sqlite'),
  )
  
  # ensure the instance folder exists
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass
  
  # a simple page that says hello
  @app.route('/hello')
  def hello():
    return 'Hello, World!'


  from . import db
  db.init_app(app)


  from . import auth
  app.register_blueprint(auth.bp)

  from . import blog
  app.register_blueprint(blog.bp)
  app.add_url_rule('/', endpoint='index')

  return app
