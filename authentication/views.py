
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from .models import Product



# Create your views here.

@never_cache
@login_required(login_url='signin')
def home(request):
    products = Product.objects.all()
    return render(request, "authentication/index.html",{'products':products})


@never_cache
def signin(request):
    
    
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            passone = request.POST['passone']
            
            user = authenticate(username=username, password=passone)  
        
            if user is not None:
                login(request,user)
            
                return redirect('home')
            else:
                messages.error(request, "Bad credentials!")
                return redirect('signin')
    
    return render(request, "authentication/signin.html")
@never_cache
def signout(request):
    logout(request)
    messages.success(request,"logged out Succesfully")
    return redirect('signin')
