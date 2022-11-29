from django.shortcuts import render,redirect
from .models import *
from . import forms
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.
def text(request):
    return render(request,'swiggy1/index.html')
def home(request):
    # foods = food.objects.all()
    #user=forms.userid()
    return render(request,'swiggy1/index.html')
def register(request):
    if request.method=='POST':
        name=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        if pass1==pass2:
            user=User.objects.create_user(username=name,email=email,password=pass1)
            user.is_staff=True
            user.is_superuser=True
            user.save()
            messages.success(request,'Registered Successfully')
            return redirect('Login')
        else:
            messages.warning(request,'Password Mismatch')
            return redirect('Register')
    else:
        form=NewUserForm()
        return render(request,'swiggy1/register.html',{'form':form})
def fooditems(request):
     foods = food.objects.all()
     return render(request,'swiggy1/fooditems.html',{'foods':foods})

def offer(request):
    return render(request,'swiggy1/offer.html')
