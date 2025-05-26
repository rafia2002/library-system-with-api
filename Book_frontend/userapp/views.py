from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already in use')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('userapp:login')
    return render(request, 'userapp/register.html')


def user_login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('userapp:home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'userapp/login.html')

@login_required(login_url='userapp:login')
def user_home(request):
    try:
        response = requests.get('http://127.0.0.1:8000/book/api/Books/')
        books = response.json() if response.status_code == 200 else []
    except:
        books = []
    return render(request, 'userapp/home.html', {'books': books})

@login_required(login_url='userapp:login')
def download_book(request, book_id):
    try:
        response = requests.get(f'http://127.0.0.1:8000/book/api/Books/{book_id}/')
        if response.status_code == 200:
            book = response.json()
            return redirect(book['file'])  # assumes the backend provides direct file URLs
    except:
        pass
    messages.error(request, 'Failed to download file.')
    return redirect('userapp:home')

def user_logout(request):
    logout(request)
    return redirect('userapp:login')


# Create your views here.
