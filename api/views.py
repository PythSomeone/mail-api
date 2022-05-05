from django.shortcuts import render

# Create your views here.
from api.models import Email, Mailbox, Template
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import MailboxSerializer, EmailSerializer, TemplateSerializer


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
    serializer_class = EmailSerializer
    permission_classes = [permissions.IsAuthenticated]

class TemplateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = [permissions.IsAuthenticated]