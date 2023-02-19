from django.contrib import admin
from .models import Asset


class AssetAdmin(admin.ModelAdmin):
    search_fields = ['type', 'brand', 'model']
    list_display = ('type', 'brand', 'model')


admin.site.register(Asset, AssetAdmin)
