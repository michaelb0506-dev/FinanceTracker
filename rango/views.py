from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from rango.models import Account,User,Transaction
from rango.forms import AccountForm, TransactionForm

from django.http import HttpResponse

@login_required
def home(request):
    accounts = Account.objects.filter(user = request.user)
    return render(request, 'rango/home.html', {"accounts":accounts})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'rango/login.html', {"error": "Invalid Username or Password"})
    else:
        return render(request, 'rango/login.html')
    
@login_required
def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            new_account = form.save(commit=False)
            new_account.user = request.user
            new_account.save()
            return redirect('rango:home')
        else:
            return render(request, 'rango/create_account.html' ,{"accountform":form})
    else:
        accountform = AccountForm()
        return render(request, 'rango/create_account.html', {"accountform":accountform})

@login_required
def account_page(request, account_id):
    account = get_object_or_404(Account, user = request.user, id = account_id)
    transactions = Transaction.objects.filter(account = account)
    return render(request, 'rango/accounts.html', {"transactions":transactions, "account":account})

@login_required
def add_transaction(request, account_id):
    account = get_object_or_404(Account, user=request.user, id=account_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.account = account
            new_transaction.save()
            return redirect('rango:account_page', account_id = account.id)
        else:
            return render(request, 'rango/add_transaction.html', {"transactionform": form, "account" : account})
    else:
        transactionform = TransactionForm()
        return render(request, 'rango/add_transaction.html', {"transactionform": transactionform, "account": account})
    
       

