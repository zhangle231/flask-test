from flask import Flask
from celery import Celery
from celery.schedules import crontab

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


flask_app = Flask(__name__)
flask_app.config.update(
                CELERY_BROKER_URL='pyamqp://guest:guest@localhost:5672//',
                CELERY_RESULT_BACKEND='rpc://'
                )

celery = make_celery(flask_app)

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )

cnt = {}
cnt['cnt'] = 1

@celery.task
def test(arg):
    tmp = cnt['cnt'] + 1
    cnt['cnt'] = tmp
    print(str(tmp))
    print(arg)

@celery.task()
def add_together(a, b):
    tmp = cnt['cnt']
    return tmp
