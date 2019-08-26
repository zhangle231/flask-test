#from celery import Celery

#app=Celery('tasks',broker='pyamqp://guest:guest@localhost:5672//')
#app=Celery('tasks', backend='rpc://', broker='pyamqp://guest:guest@localhost:5672//')

#@app.task
#def add(x,y):
#    return x + y
from celery import Celery
from celery.schedules import crontab

#app = Celery()
app=Celery('tasks', backend='rpc://', broker='pyamqp://guest:guest@localhost:5672//')

@app.on_after_configure.connect
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

@app.task
def test(arg):
    tmp = cnt['cnt'] + 1
    cnt['cnt'] = tmp
    print(str(tmp))
    print(arg)
