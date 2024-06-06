from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
  dishes = Dish.objects.all()
  return render(request, "home.html", {'dishes':dishes})

def signup(request):
  if request.method == "POST":
    username = request.POST.get('username')
    email = request.POST.get('email')  
    password = request.POST.get('password')
    c_password = request.POST.get('c_password')

    if password == c_password:
      if User.objects.filter(username=username).exists():
        messages.info(request, f"Username already exists")
        return redirect('signup')

      if User.objects.filter(email=email).exists():
          messages.info(request, f"Email already exists")
          return redirect('signup')

      user = User.objects.create_user(username=username, email=email, password=password)
      user = authenticate(username=username, email=email, password=password)
      user.save()
      return redirect('login')
    return redirect('login')  
  return render(request, "signup.html") 

def login(request):
  if request.user.is_authenticated :
      return redirect('home')

  if request.method == "POST":
    username = request.POST.get('username')
    email = request.POST.get('email')  
    password = request.POST.get('password')

    user = auth.authenticate(username=username, email=email, password=password)
    if user is not None:
      auth.login(request, user)
      return render(request, "home.html")
    else:
      messages.info(request, "Enter correct details")
      return redirect('login')  
  return render(request, "login.html")

def logout(request):
  auth.logout(request)
  return redirect('login')

def add_product(request):
  if request.method == "POST":
    name = request.POST.get('name')
    description = request.POST.get('description')
    price = request.POST.get('price')
    if name and description and price :
      Product.objects.create(name=name, description=description, price=price)
    else:
      messages.info(request, "Enter details")  
  return render(request, "add_product.html") 

def admins(request):
    is_admin = request.user.groups.filter(name='Admin').exists()
    return render(request, "admins.html")

def ordered_foods(request):
  return render(request, "ordered_foods.html") 

def payment(request):
  return render(request, "payment.html")  

def about(request):
  return render(request, "about.html")             