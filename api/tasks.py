from api.celery import app

from api.send_email import send_email


@app.task
def send_email_task(email_id):
    return send_email(email_id)

