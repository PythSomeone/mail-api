from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'mailboxes', views.MailboxViewSet)
router.register(r'emails', views.EmailViewSet)
router.register(r'templates', views.TemplateViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]