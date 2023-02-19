from django.urls import path, include
from rest_framework import routers
from .views import AdministrativeDocumentViewSet


app_name = 'api'

router = routers.SimpleRouter()
router.register('admin_document', AdministrativeDocumentViewSet, basename='admin-document')

urlpatterns = [
    path('', include(router.urls)),
]

