from celery import Celery
from time import sleep

app = Celery('tasks', broker='pyamqp://guest@localhost:5672',
             backend='redis://127.0.0.1:6379/0')


@app.task
def add(x, y):
    sleep(15)
    return x + y
