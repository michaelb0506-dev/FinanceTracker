from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from rango.models import Account,User
from rango.forms import AccountForm

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
       

