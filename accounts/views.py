from django.shortcuts import render, redirect
from . models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy, reverse
from django.contrib.auth.hashers import check_password
from django.db.models import Q, F

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'loan_app/register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        custom_role = request.POST['userType']

        myuser = User.objects.create(username=username, email=email, custom_role=custom_role)
        myuser.set_password(pass1)
        myuser.save()
        
        messages.success(request, "Your Account has been created Successfully!")
        
        return redirect('signin')
    
    return render(request, 'loan_app/register.html', {'messages':messages})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid Credentials')
            return redirect('signin')    
            
        if user is not None:
            login(request,user)
            return redirect(reverse('predict'))
        
        else:
            messages.error(request, "Bad Credentials")
            return redirect('signin')    
    return render(request, 'loan_app/login.html')

def signout(request):
    logout (request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('index')


