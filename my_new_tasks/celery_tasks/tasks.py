from celery import shared_task
import time


@shared_task
def task_handler():
    time.sleep(3)
    print("Hello")
