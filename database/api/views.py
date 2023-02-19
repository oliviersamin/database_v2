from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    UserSerializer,
    UserDetailSerializer
)
from .utils.queries import get_and_filtered_results

class UserViewSet(ModelViewSet):
    """ manage all the views related to the user default Django model """
    serializer_class = UserSerializer
    detail_serializer_class = UserDetailSerializer

    def get_queryset(self):
        params = self.request.query_params
        query = User.objects.all()
        if params:
            filtered_results = get_and_filtered_results(params, query)
        query = User.objects.filter(pk__in=filtered_results)
        return query
