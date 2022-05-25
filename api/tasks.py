from django.conf import settings
from celery import shared_task

from api import send_email

@shared_task(name='send_email_task')
def send_email_task(email):
    return send_email(email)