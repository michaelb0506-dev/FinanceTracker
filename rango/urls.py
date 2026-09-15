from django.urls import path
from rango import views
from django.contrib.auth import views as auth_views

app_name = 'rango'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create_account/', views.create_account, name='create_account'),
    path('accounts/<int:account_id>/',views.account_page, name='account_page'),
    path('accounts/<int:account_id>/add_transaction/', views.add_transaction, name='add_transaction'),
    path('create_category/<int:account_id>/', views.create_category, name='create_category'),
]