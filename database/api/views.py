from django.shortcuts import render
from django.db.models import Q
from administrative.models import Document
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    AdminDocumentSerializer,
)
from .utils.queries import get_and_filtered_results


class AdministrativeDocumentViewSet(ModelViewSet):
    """ manage views related to the Administrative Document model """
    serializer_class = AdminDocumentSerializer

    def get_queryset(self):
        params = self.request.query_params
        query = Document.objects.all()
        if params:
            filtered_results = get_and_filtered_results(params, query)
            query = Document.objects.filter(pk__in=filtered_results)
        return query
