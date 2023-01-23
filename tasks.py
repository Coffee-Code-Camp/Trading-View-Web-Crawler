from celery_app import app
from lib.recources import get_symbols, get_intervals
from lib.get_data import get_data

@app.task
def crawl_all():
    for s in get_symbols():
        for i in get_intervals():
            data = get_data(s, i)
            print(data)