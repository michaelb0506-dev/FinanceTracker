from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    account_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.account_name

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()
    is_income = models.BooleanField(default=True)  
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.amount} - {self.category} - {self.date}"
