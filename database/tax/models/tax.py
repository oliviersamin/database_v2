from django.db import models
from django.contrib.auth.models import User


def get_tax_choices():
    return [('Real Estate tax', 'Real Estate tax'), ('Transportation tax', 'Transportation tax'), ('Person tax', 'Person tax'), ('Other tax', 'Other tax')]


class Tax(models.Model):
    """
    'Tax'
    """
    name = models.CharField(max_length=100, blank=True, null=True)
    tax_type = models.CharField(max_length=50, null=True, blank=True, choices=get_tax_choices())
    real_estate_asset = models.ForeignKey('real_estate.Asset', blank=True, null=True, related_name='tax', on_delete=models.CASCADE, help_text="Fill only if type = Real Estate tax")
    transportation_asset = models.ForeignKey('transportation.Asset', blank=True, null=True, related_name='tax', on_delete=models.CASCADE, help_text="Fill only if type = Transportation tax")
    person = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='tax', help_text="Fill only if type = Person tax")
    is_tax_management_company_used = models.BooleanField(null=True, blank=True, default=False)
    tax_management_company = models.ForeignKey('tax.TaxManagementCompany', blank=True, null=True, on_delete=models.CASCADE, related_name='tax', help_text='Fill only if is_tax_management_company_used is True')
    personal_email_used = models.EmailField(null=True, blank=True)
    site_app = models.CharField(max_length=70, blank=True, null=True, help_text="ex: impots.gouv.fr")
    annual_price = models.JSONField(null=True, blank=True, help_text="ex: {'2020': 400, '2021': 400, ...}")
    payment_proof = models.JSONField(null=True, blank=True, help_text="ex: {'2020': 'receipt_number0987y76t', '2021': 'receipt_number1237g76t'}")

    class Meta:
        ordering = ['name', 'tax_type']
        verbose_name_plural = "Taxes"

    def __str__(self):
        return self.name + ' - ' + self.asset_type
