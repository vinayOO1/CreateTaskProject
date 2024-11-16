import time

from my_new_tasks.celery import app


@app.task(name="CREATE_TASK_HANDLER")
def task_handler(data={}):
    time.sleep(3)
    print("Hello")


def custom_celery_handler(data={}):
    task_handler.delay()
