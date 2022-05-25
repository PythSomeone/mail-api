from time import timezone
import uuid
from django.db import models

from django.contrib.postgres.fields import ArrayField
from django.core import serializers


import logging

from api.tasks import send_email_task
# logger = logging.getLogger(django)

# Create your models here.
 
class Mailbox(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.CharField(max_length=255)
    port = models.IntegerField(default=465)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    use_ssl = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    date = models.DateTimeField()
    last_update = models.DateTimeField()

    @property
    def sent(self):
        "Returns amount of sent messages by the user."
        return '%s %s' % (self.first_name, self.last_name)

class Template(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=255)
    text = models.TextField()
    attachment = models.FileField(blank=True, null=True)
    date = models.DateTimeField()
    last_update = models.DateTimeField()

class Email(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mailbox = models.ForeignKey(Mailbox, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    to = ArrayField(models.CharField(max_length=255), default=list, null=True)
    cc = ArrayField(models.CharField(max_length=255), default=list, null=True)
    bcc = ArrayField(models.CharField(max_length=255), default=list, null=True)
    reply_to = models.EmailField()
    sent_date = models.DateTimeField()
    date = models.DateTimeField()

    def __str__(self):
        return str(self.id)

    # def save(self):
    #     if self.id:
    #         old_foo = Foo.objects.get(pk=self.id)
    #         if old_foo.YourBooleanField == False and self.YourBooleanField == True:
    #             send_email()
    #     super(Foo, self).save()

    def save(self, *args, **kwargs):
        super(Email, self).save(*args, **kwargs)
        if self.mailbox.is_active:
            send_email_task.delay(serializers.serialize('json', Email.objects.filter(pk=self.id)))
        else:
            # logger.error('Failed to send the email with id: '+ str(self.id) 
            # + ' from mailbox with id: '+ str(self.mailbox.id)
            # + ', mailbox is not active')
            pass
        super(Email, self).save()
