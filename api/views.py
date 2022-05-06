from django.shortcuts import render

# Create your views here.
from api.models import Email, Mailbox, Template
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Prefetch
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
    http_method_names = ['get', 'delete', 'post']
    # def destroy(self, request, *args, **kwargs):
    #     logedin_user = request.user
    #     if(logedin_user == "admin"):
    #         email = self.get_object()
    #         email.delete()
    #         response_message = {"message": "Item has been deleted"}
    #     else:
    #         response_message = {"message": "Not Allowed"}

    #     return Response(response_message)



class TemplateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = [permissions.IsAuthenticated]

