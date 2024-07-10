from django.db import models
from django.conf import settings  # Import settings to reference AUTH_USER_MODEL

class Budget(models.Model):
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='budgets')

    def __str__(self):
        return self.name

class Income(models.Model):
    source = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='incomes')

    def __str__(self):
        return self.source

class Report(models.Model):
    report_type = models.CharField(max_length=100)
    period_start = models.DateField()
    period_end = models.DateField()
    generated_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports')

    def __str__(self):
        return f"{self.report_type} - {self.generated_on}"

class Expenses(models.Model):
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='expenses')

    def __str__(self):
        return f"{self.category} - {self.amount}"
