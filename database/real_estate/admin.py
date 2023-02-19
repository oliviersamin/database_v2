from django.contrib import admin
from .models import (
    Asset,
    CoproManagementCompany,
    CoproManagementContract,
    Mortgage,
    RentingManagementCompany,
    RentingManagementContract,
    Tenant
)
from .actions import Results


def get_year_data_for_renting_admin(modeladmin, request, queryset):
    data = Results().handle(request)
    instance = queryset.first()
    instance.annual_results[list(data.keys())[0]] = list(data.values())[0]
    instance.save()
get_year_data_for_renting_admin.short_description = 'get year results and details - take 30 seconds'


class AssetAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'nickname', 'city']
    list_display = ('owner', 'nickname', 'city', 'buying_price', 'has_on_going_mortgage')
    actions = [get_year_data_for_renting_admin]


class CoproCompanyAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ('name',)


class CoproContractAdmin(admin.ModelAdmin):
    search_fields = ['company', 'is_management_active']
    list_display = ('company', 'is_management_active')


class MortgageAdmin(admin.ModelAdmin):
    search_fields = ['asset', 'name']
    list_display = ('asset', 'name')


class RentingCompanyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)


class RentingContractAdmin(admin.ModelAdmin):
    search_fields = ['company']
    list_display = ('company',)


class TenantAdmin(admin.ModelAdmin):
    search_fields = ['asset', 'last_name', 'first_name', 'is_actual_tenant']
    list_display = ('is_actual_tenant', 'asset', 'last_name', 'first_name')


admin.site.register(Asset, AssetAdmin)
admin.site.register(CoproManagementCompany, CoproCompanyAdmin)
admin.site.register(CoproManagementContract, CoproContractAdmin)
admin.site.register(RentingManagementCompany, RentingCompanyAdmin)
admin.site.register(RentingManagementContract, RentingContractAdmin)
admin.site.register(Mortgage, MortgageAdmin)
admin.site.register(Tenant, TenantAdmin)
