import os
from django.db import models
from django.contrib.auth.models import User
from dotenv import load_dotenv
load_dotenv()


def get_types():
    return [('ID card', 'ID card'), ('Passport', 'Passport'), ('driving licence', 'driving licence'), ('ticket', 'ticket'), ('other', 'other')]


class Document(models.Model):
    """
    'Document'
    """
    UPLOADED_FILE_PATH = os.environ.get('UPLOADING_FILES_FOLDER_PATH')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True, choices=get_types())
    file_path = models.FilePathField(blank=True, null=True, path=UPLOADED_FILE_PATH, recursive=True)
    comment = models.JSONField(null=True, blank=True)

    class Meta:
        ordering = ['type', 'name']
        verbose_name_plural = "Documents"

    def __str__(self):
        return self.name + ' - ' + self.type if self.name else self.type

    def get_user_name(self):
        return self.user.get_full_name()