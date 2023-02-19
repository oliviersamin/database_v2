from django.contrib import admin
from .models import (
    Tax,
    TaxManagementCompany,
    TaxManagementContract
)


class TaxContractAdmin(admin.ModelAdmin):
    search_fields = ['company', 'is_contract_active']
    list_display = ('company', 'is_contract_active', 'annual_price')


class TaxCompanyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)


class TaxAdmin(admin.ModelAdmin):
    search_fields = ['name', 'tax_type']
    list_display = ('name',  'tax_type', 'annual_price')


admin.site.register(TaxManagementContract, TaxContractAdmin)
admin.site.register(TaxManagementCompany, TaxCompanyAdmin)
admin.site.register(Tax, TaxAdmin)
