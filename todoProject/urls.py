"""
URL configuration for todoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import debug_toolbar
from django.conf import settings
from authApp import views
from todoApp import views as views2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('authApp.urls')),
    path('accounts/login/',views.loginView,name='login'),
    path('accounts/logout/',views.logoutView,name='logout'),
    path('accounts/register/',views.registerView,name='register'),
    path('tasks/',include('todoApp.urls',namespace=('todoApp')))
]

if settings.DEBUG:
    urlpatterns+=[
        path('__debug__/',include(debug_toolbar.urls)),
    ]
