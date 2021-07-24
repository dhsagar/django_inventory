from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import AddEditForm, ProductForm

# Create your views here.
def LoginView(request): #login page
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home-Page')
        else:
            messages.info(request,'Incorrect Username or Password')
    return render(request, 'InventoryProjectApp/loginview.html')

def RegistrationView(request): #login page
    return render(request, 'InventoryProjectApp/registrationview.html')

def MainView(request):
    products = Product.objects.all()
    return render(request, 'InventoryProjectApp/mainview.html', {'products':products})

def productForm(request):
    form = ProductForm()
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('../main/')
    context ={
        'form': form
    }
    return render(request, 'InventoryProjectApp/product_form.html', context)

def updateForm(request, pk):
    product=Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    context ={
        'form': form
    }
    if request.method=='POST':
        form=ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return  redirect('../main/')
    return render(request, 'InventoryProjectApp/product_form.html', context)

def HomePage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Main-Page-New')
        else:
            messages.info(request,'Incorrect Username or Password')
    return render(request, 'InventoryProjectApp/homepage.html')

def MainPage(request):
    products = Product.objects.all()
    product_count = products.count()
    damage_count = Product.objects.filter(status='Damaged').count()
    context={
        'products':products,
        'product_count':product_count,
        'damage_count':damage_count

    }
    return render(request, 'InventoryProjectApp/mainpage.html', context)

def AddItemForm(request):
    form = AddEditForm()
    if request.method=='POST':
        form=AddEditForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('Main-Page-New')
    context ={
        'form': form
    }
    return render(request, 'InventoryProjectApp/AddEditItem.html', context)

def EditItemForm(request, pk):
    product=Product.objects.get(id=pk)
    form = AddEditForm(instance=product)
    context ={
        'form': form
    }
    if request.method=='POST':
        form=AddEditForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return  redirect('Main-Page-New')
    return render(request, 'InventoryProjectApp/AddEditItem.html', context)

def LogoutView(request):
    logout(request)
    return redirect('Home-Page')
