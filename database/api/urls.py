from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet


app_name = 'api'

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]

