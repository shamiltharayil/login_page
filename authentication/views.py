
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib.auth.decorators import user_passes_test
from . forms import UserUpdation



# Create your views here.

@never_cache
@login_required(login_url='signin')
def home(request):
    products = Product.objects.all()
    return render(request, "authentication/index.html",{'products':products})

@never_cache
def signup(request):
    if request.method == "POST":
        
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        passone = request.POST['passone']
        passtwo = request.POST['passtwo']

        myuser = User.objects.create_user(username, email, passone,passtwo)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "your Account has been succesfully created")

        return redirect('signin')

    return render(request, "authentication/signup.html")

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


@never_cache
@login_required(login_url='signin')
@user_passes_test(lambda u: u.is_superuser)
def showadmin(request):
    users=User.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        users = User.objects.filter(username__icontains=q)
    return render(request,"authentication/showadmin.html",{'users':users})

#UPDATE 
@never_cache
@login_required(login_url='index')
def update(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = UserUpdation(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect("showadmin")
    else:
        pi = User.objects.get(pk=id)
        fm = UserUpdation(instance=pi)
    return render(request,'authentication/update.html',{'form':fm})

# DELETE
@never_cache
def delete(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect("showadmin")