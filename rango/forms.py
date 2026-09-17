from django import forms
from rango.models import Account, Transaction, Category
from django.contrib.auth.forms import UserCreationForm

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_name']
        widgets = {
            'account_name': forms.TextInput(attrs={'class': 'form-control'})
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'category', 'date', 'is_income', 'description']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'is_income': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset= Category.objects.filter(user=user)

class CategoryForm(forms.ModelForm):
    class Meta:
         model = Category
         fields = ['name']
         widgets = {
             'name': forms.TextInput(attrs={'class': 'form-control'})
         }

class StyledUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'