from time import timezone
import uuid
from django.db import models

from django.contrib.postgres.fields import ArrayField

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
    to = ArrayField(models.CharField(max_length=255))
    cc = ArrayField(models.CharField(max_length=255))
    bcc = ArrayField(models.CharField(max_length=255))
    reply_to = models.EmailField()
    sent_date = models.DateTimeField()
    date = models.DateTimeField()