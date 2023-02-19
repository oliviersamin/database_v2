from django.db import models
from django.contrib.auth.models import User


class CoproManagementCompany(models.Model):
    """
    Copro management company model
    """
    name = models.CharField(max_length=50, blank=True, null=True)
    personal_email_used = models.EmailField(null=True, blank=True)
    site_app_company = models.CharField(max_length=70, blank=True, null=True, help_text="ex: myfoncia.com")

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Copro Management Companies"

    def __str__(self):
        return self.name


class CoproManagementContract(models.Model):
    """
    Copro management contract model
    """
    company = models.OneToOneField('real_estate.CoproManagementCompany', related_name='copro_contract', blank=False, null=True, on_delete=models.CASCADE)
    contract_number = models.CharField(max_length=50, blank=True, null=True)
    starting_date = models.DateField(blank=True, null=True)
    ending_date = models.DateField(blank=True, null=True)
    is_management_active = models.BooleanField(null=True, blank=True)
    annual_expenses = models.JSONField(null=True, blank=True, help_text="ex: {'2020': {'fixed': 1400, 'refurbishment': 300, 'other': 12, 'payment_delay': 100}}")

    class Meta:
        ordering = ['company__name', 'is_management_active']
        verbose_name_plural = "Copro Management Contracts"

    def __str__(self):
        return self.company.name
