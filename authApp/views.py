from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def registerView(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():

            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            email=form.cleaned_data.get('email')
            
            user=User.objects.create_user(username=username,password=password,email=email)
            login(request,user)
            return redirect('home')
            
    else:
        form=RegisterForm()
    return render(request,'accounts/register.html',{'form':form})

def loginView(request):
    if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                next_url=request.POST.get('next') or request.GET.get('next') or 'home'
                return redirect(next_url)
            else:
                return render(request,'accounts/login.html',{'error':'Invalid Credentials'})
    return render(request,'accounts/login.html')

def logoutView(request):
    if request.method=='POST':
        logout(request)
        return redirect('login')
    return render(request,'accounts/logout.html')

@login_required
def homeView(request):
    return render(request,'home/index.html')