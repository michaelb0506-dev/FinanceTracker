import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FinanceTracker.settings')
django.setup()

from django.contrib.auth.models import User
from rango.models import Account, Category, Transaction
from datetime import date
from decimal import Decimal

def populate():
    
    User.objects.all().delete()

    user = User.objects.create_user(username='testuser', password='testpassword')

    food = Category.objects.create(name='Food', user=user)
    salary = Category.objects.create(name='Salary', user=user)
    rent = Category.objects.create(name='Rent', user=user)
    entertainment = Category.objects.create(name='Entertainment', user=user)
    transport = Category.objects.create(name='Transport', user=user)
    starting_balance = Category.objects.create(name='Starting Balance',user = user)

    current_account = Account.objects.create(account_name='Current Account', user=user)
    savings_account = Account.objects.create(account_name='Savings Account', user=user)

    Transaction.objects.create(amount=Decimal('500.00'), category=starting_balance, date=date(2026, 1, 1), is_income=True, account=savings_account, description='Initial Deposit')

    months = [1, 2, 3, 4, 5, 6]
    for month in months:
        Transaction.objects.create(amount=Decimal('2000.00'), category=salary, date=date(2026, month, 1), is_income=True, account=current_account, description=f'{date(2026, month, 1).strftime("%B")} Salary')
        Transaction.objects.create(amount=Decimal('800.00'), category=rent, date=date(2026, month, 2), is_income=False, account=current_account, description='Monthly Rent')
        Transaction.objects.create(amount=Decimal('150.00') + Decimal(month * 5), category=food, date=date(2026, month, 10), is_income=False, account=current_account, description='Groceries')
        Transaction.objects.create(amount=Decimal('60.00'), category=transport, date=date(2026, month, 15), is_income=False, account=current_account, description='Train Pass')
        Transaction.objects.create(amount=Decimal('40.00') + Decimal(month * 3), category=entertainment, date=date(2026, month, 20), is_income=False, account=current_account, description='Cinema & Subscriptions')

    # A couple of savings top-ups over time
    Transaction.objects.create(amount=Decimal('200.00'), category=salary, date=date(2026, 3, 5), is_income=True, account=savings_account, description='Savings Top-up')
    Transaction.objects.create(amount=Decimal('300.00'), category=salary, date=date(2026, 6, 5), is_income=True, account=savings_account, description='Savings Top-up')

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
    print("Rango population script completed.")