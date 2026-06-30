from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    AccountName = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.AccountName

class Transaction(models.Model):
    ammount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    dictate = models.DateTimeField(auto_now_add=True)
    type = models.BooleanField(default=True)  
    accountID = models.ForeignKey(Account, on_delete=models.CASCADE)
