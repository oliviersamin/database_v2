from django.contrib import admin
from .models import (
    BankAccount,
    BankCard,
    Bank
)


class BankAccountAdmin(admin.ModelAdmin):
    search_fields = ['bank', 'IBAN', 'is_account_open']
    list_display = ('bank', 'IBAN', 'is_account_open')


class BankCardAdmin(admin.ModelAdmin):
    search_fields = ['bank_acount', 'name', 'is_active']
    list_display = ('name', 'is_active', 'bank_account', 'ending_date')


class BankAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)


admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(BankCard, BankCardAdmin)

