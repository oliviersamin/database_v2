from django.contrib import admin
from .models import (
    Document,
    InsuranceContract,
    InsuranceCompany
)


class DocumentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'type', 'user']
    list_display = ('user', 'type', 'name')


class InsuranceCompanyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'phone_number')


class InsuranceContractAdmin(admin.ModelAdmin):
    search_fields = ['company']
    list_display = ('company', 'type', 'is_insurance_active')


admin.site.register(Document, DocumentAdmin)
admin.site.register(InsuranceContract, InsuranceContractAdmin)
admin.site.register(InsuranceCompany, InsuranceCompanyAdmin)
