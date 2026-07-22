import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FinanceTracker.settings')
django.setup()

from django.contrib.auth.models import User
from rango.models import Account, Category, Transaction
from datetime import date
from decimal import Decimal

def populate():
    
    User.objects.filter(username='testuser').delete()

    user = User.objects.create_user(username='testuser', password='testpassword')

    food = Category.objects.create(name='Food')
    salary = Category.objects.create(name='Salary')
    starting_balance = Category.objects.create(name='Starting Balance')

    current_account = Account.objects.create(account_name='Current Account', user=user)
    savings_account = Account.objects.create(account_name='Savings Account', user=user)

    Transaction.objects.create(amount=Decimal('2000.00'), category=salary, date=date(2026,1,1), is_income=True, account=current_account, description='January Salary')
    Transaction.objects.create(amount=Decimal('50.00'), category=food, date=date(2026,1,2), is_income=False, account=current_account, description='Groceries')
    Transaction.objects.create(amount=Decimal('500.00'), category=starting_balance, date=date(2026,1,1), is_income=True, account=savings_account, description='Initial Deposit')


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
    print("Rango population script completed.")