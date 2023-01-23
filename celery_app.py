from celery import Celery
from random import randint

app = Celery('tasks', broker='redis://0.0.0.0:6379', backend='redis://0.0.0.0:6379')


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.crawl_all',
        'schedule': 30
    },
}