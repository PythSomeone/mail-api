from django.shortcuts import render
import logging
# Create your views here.
from api.models import Email, Mailbox, Template

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


from api.serializers import MailboxSerializer, EmailSerializer, TemplateSerializer
from api.tasks import send_email_task


class MailboxViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Mailbox.objects.all()
    serializer_class = MailboxSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Email.objects.all()
    mailbox = Mailbox.objects.all()
    template = Template.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'delete', 'post']

    def perform_create(self, serializer):
        instance = serializer.save()
        mail = Email.objects.filter(pk=instance.id)
        if instance.mailbox.is_active:
            send_email_task.delay(instance.id)

        else:
            # logger.error('Failed to send the email with id: '+ str(self.id) 
            # + ' from mailbox with id: '+ str(self.mailbox.id)
            # + ', mailbox is not active')
            pass

class TemplateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = [permissions.IsAuthenticated]

