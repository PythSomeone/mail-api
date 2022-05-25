from django.core.mail import EmailMultiAlternatives
from rest_framework import serializers
from django.forms.models import model_to_dict

import json

def send_email(mail):

    data = mail
    template = data.template
    mailbox = data.mailbox

    email = EmailMultiAlternatives(
        subject = template.subject,
        body = template.text,
        to = email.to,
        cc = email.cc,
        from_email=mailbox.from_email,
        bcc=data.bcc,
        attachments=template.attachment,
        reply_to=data.reply_to
    )
    return email.send(fail_silently=False)