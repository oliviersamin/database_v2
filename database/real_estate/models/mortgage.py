from django.db import models
from django.contrib.auth.models import User


class Mortgage(models.Model):
    """
    'Mortgage'
    """
    asset = models.OneToOneField('real_estate.Asset', related_name='mortgage', blank=False, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    bank_account = models.ForeignKey('finances.BankAccount', null=True, blank=True, on_delete=models.CASCADE)
    starting_date = models.DateField(blank=True, null=True)
    ending_date = models.DateField(blank=True, null=True)
    rate_renegociations = models.JSONField(null=True, blank=True, help_text="ex: {'2020': 2%, '2021': 1.8%}")
    annual_interests = models.JSONField(null=True, blank=True, help_text="ex: {'2020': 2500, '2021': 2200}")
    annual_capital_refund = models.JSONField(null=True, blank=True, help_text="ex: {'2020': 4000, '2021': 4300}")
    capital_due_end_of_year = models.JSONField(null=True, blank=True, help_text="ex: {'2020': 112345, '2021': 108356}")

    class Meta:
        ordering = ['asset', 'name']
        verbose_name_plural = "Mortgages"

    def __str__(self):
        return self.name + ' - ' + self.asset
