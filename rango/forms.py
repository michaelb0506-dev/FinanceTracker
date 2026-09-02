from django import forms
from rango.models import Account, Transaction

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_name']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'category', 'date', 'is_income', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }