from django.db import models


class InsuranceCompany(models.Model):
    """
    'Insurance Company'
    """
    name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.PositiveIntegerField(null=True, blank=False)
    site_app_company = models.CharField(max_length=70, blank=True, null=True, help_text="ex: myfoncia.com")

    class Meta:
        ordering = ['name', 'phone_number']
        verbose_name_plural = "Insurance Companies"

    def __str__(self):
        return self.name
