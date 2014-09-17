"""
*Test the ETA functionality of celery
"""

from celery import Celery

app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task()
def echo(task_number):
    print task_number