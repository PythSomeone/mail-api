from api.models import Email, Mailbox, Template
from rest_framework import serializers


class MailboxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mailbox
        fields = [
            'id',
            'host',
            'port',
            'login',
            'password',
            'email_from',
            'use_ssl',
            'is_active',
            'date',
            'last_update',
            ]
class ArrayField(serializers.ListField):
    child = serializers.CharField(max_length=255, allow_blank=True)

class EmailSerializer(serializers.HyperlinkedModelSerializer):
    sent_date = serializers.DateTimeField()
    date = serializers.DateTimeField()
    class Meta:
        model = Email
        fields = (
            'id',
            'mailbox',
            'template',
            'to',
            'cc',
            'bcc',
            'reply_to',
            'sent_date',
            'date',
        )

class TemplateSerializer(serializers.HyperlinkedModelSerializer):
    date = serializers.DateTimeField()
    last_update = serializers.DateTimeField()
    class Meta:
        model = Template
        fields = [
    'id',
    'subject',
    'text',
    'date',
    'last_update',
    ]