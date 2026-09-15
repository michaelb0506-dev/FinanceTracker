from django import forms
from rango.models import Account, Transaction, Category

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

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset= Category.objects.filter(user=user)

class CategoryForm(forms.ModelForm):
    class Meta:
         model = Category
         fields = ['name']