from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'mailbox', views.MailboxViewSet)
router.register(r'template', views.TemplateViewSet)
router.register('email', views.EmailViewSet, basename='emails')

urlpatterns = [
    path(r'api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]