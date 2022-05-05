import uuid
from django.db import models

# Create your models here.
 
class Mailbox(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.CharField()
    port = models.IntegerField(default=465)
    login = models.CharField()
    password = models.CharField()
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
    subject = models.CharField()
    port = models.TextField(required=True)
    attachment = models.FileField()
    date = models.DateTimeField()
    last_update = models.DateTimeField()

class Email(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mailbox = models.CharField()
    mailbox = models.ForeignKey(Mailbox, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    to = models.ArrayField(base_field=[])
    cc = models.ArrayField(base_field=[])
    bcc = models.ArrayField(base_field=[])
    reply_to = models.EmailField()
    sent_date = models.DateTimeField
    date = models.DateTimeField('data_utworzenia', auto_now=True)