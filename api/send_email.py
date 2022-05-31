from django.core.mail import EmailMultiAlternatives

from api.models import Email
from django.core.mail import get_connection



def send_email(mail_id):

    data = Email.objects.filter(pk=mail_id).get()
    template = data.template
    mailbox = data.mailbox

    email = EmailMultiAlternatives(
        subject = template.subject,
        body = template.text,
        to = tuple(map(str, 'example@gmail.com'.split(', '))),
        cc = data.cc,
        from_email=str(mailbox.login + "@"+ mailbox.host),
        bcc=data.bcc,
        attachments=template.attachment,
        reply_to=tuple(map(str, data.reply_to.split(', '))),
        connection= get_connection(backend='django.core.mail.backends.smtp.EmailBackend'),
    )
    return email.send(fail_silently=False)
