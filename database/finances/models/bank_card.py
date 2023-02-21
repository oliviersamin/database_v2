from django.db import models


class BankCard(models.Model):
    """
    'Bank Card'
    """
    bank_account = models.ForeignKey('finances.BankAccount', related_name='card', blank=False, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True, blank=True)
    is_active = models.BooleanField(null=True, blank=False, default=True)
    card_number = models.CharField(max_length=16, null=True, blank=True)
    ending_date = models.DateField(blank=True, null=True)
    CCV = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['bank_account__bank__name', 'name', 'card_number', 'ending_date', 'CCV']
        verbose_name_plural = "Bank Cards"

    def __str__(self):
        return self.bank.name if not self.name else self.name
