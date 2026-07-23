from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from rango.models import Account

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
          
       

