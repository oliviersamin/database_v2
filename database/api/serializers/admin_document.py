from administrative.models import Document
from rest_framework import serializers


class AdminDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['get_user_name', 'name', 'type', 'file_path', 'comment']

