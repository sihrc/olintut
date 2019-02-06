from celery import Celery

from .magic_slide1 import long_running_magic_number_generator

app = Celery('tasks', broker='pyamqp://guest@rabbitmq//', backend='redis://redis')


magic_celery_task = app.task(long_running_magic_number_generator)

"""
Run using
celery -A olintut.celery_slide3 worker
"""