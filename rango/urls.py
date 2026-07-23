from django.urls import path
from rango import views
from django.contrib.auth import views as auth_views

app_name = 'rango'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]