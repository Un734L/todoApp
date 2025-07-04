from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeView,name='home'),
    path('accounts/register/',views.registerView,name='register'),
    path('accounts/login/',views.loginView,name='login'),
    path('accounts/logout/',views.logoutView,name='logout'),
]
