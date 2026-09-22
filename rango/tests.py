from django.test import TestCase
from django.contrib.auth.models import User
from rango.models import Account, Category, Transaction
from decimal import Decimal
from datetime import date

class AccountBalanceTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.account = Account.objects.create(account_name='Test Account', user=self.user)
        self.category = Category.objects.create(name='Food', user=self.user)

    def test_balance_with_income_and_expense(self):
        Transaction.objects.create(amount=Decimal('100.00'), category=self.category, date=date(2026, 1, 1), is_income=True, account=self.account, description='Income')
        Transaction.objects.create(amount=Decimal('30.00'), category=self.category, date=date(2026, 1, 2), is_income=False, account=self.account, description='Expense')
        self.assertEqual(self.account.balance(), Decimal('70.00'))

    def test_balance_with_no_transactions(self):
        self.assertEqual(self.account.balance(), 0)


class AccountAccessTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='testpass')
        self.user2 = User.objects.create_user(username='user2', password='testpass')
        self.account1 = Account.objects.create(account_name='User1 Account', user=self.user1)

    def test_user_cannot_access_other_users_account(self):
        self.client.login(username='user2', password='testpass')
        response = self.client.get(f'/accounts/{self.account1.id}/')
        self.assertEqual(response.status_code, 404)

    def test_owner_can_access_own_account(self):
        self.client.login(username='user1', password='testpass')
        response = self.client.get(f'/accounts/{self.account1.id}/')
        self.assertEqual(response.status_code, 200)