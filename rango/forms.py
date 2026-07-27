from django import forms
from rango.models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_name']