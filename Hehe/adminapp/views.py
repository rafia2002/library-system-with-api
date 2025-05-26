from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Book
from .forms import BookForm


def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('adminapp:list_books')
        else:
            error = "Invalid credentials or not authorized"
            return render(request, 'adminapp/login.html', {'error': error})
    return render(request, 'adminapp/login.html')

@login_required(login_url='adminapp:login')
def list_books(request):
    books = Book.objects.all()
    return render(request, 'adminapp/list_books.html', {'books': books})

@login_required(login_url='adminapp:login')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")
            return redirect('adminapp:list_books')
        else:
            messages.error(request, "Failed to add book. Please check the form for errors.")
    else:
        form = BookForm()
    return render(request, 'adminapp/add_book.html', {'form': form})

@login_required(login_url='adminapp:login')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('adminapp:list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'adminapp/edit_book.html', {'form': form})

@login_required(login_url='adminapp:login')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('adminapp:list_books')
    return render(request, 'adminapp/delete_book.html', {'book': book})

def admin_logout(request):
    logout(request)
    return redirect('adminapp:login')

