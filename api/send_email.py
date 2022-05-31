from django.core.mail import EmailMultiAlternatives

from api.models import Email
from django.core.mail import get_connection
from django.core.mail.backends.smtp import EmailBackend



def send_email(mail_id):

    email = Email.objects.filter(pk=mail_id).get()
    template = email.template
    mailbox = email.mailbox

    email = EmailMultiAlternatives(
        subject = template.subject,
        body = template.text,
        to = tuple(map(str, email.to[0].split(', '))),
        cc = tuple(map(str, email.cc[0].split(', '))),
        bcc= tuple(map(str, email.bcc[0].split(', '))),
        from_email=mailbox.email_from,
        attachments=template.attachment,
        reply_to=tuple(map(str, email.reply_to.split(', '))),
        connection= get_connection(        
            host=mailbox.host,
            port=mailbox.port,
            username=mailbox.login,
            password=mailbox.password,
            use_ssl=mailbox.use_ssl,
            use_tsl=False
        ),
    )
    return email.send(fail_silently=False)
