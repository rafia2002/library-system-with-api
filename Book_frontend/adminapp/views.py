from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Book
from .forms import BookForm
import requests

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
    # api = f'http://127.0.0.1:8001/book/api/Books/'
    # books = requests.get(api)
    try:
        response = requests.get('http://127.0.0.1:8000/book/api/Books/')
        if response.status_code == 200:
            books = response.json()
        else:
            books = []
            print("Backend error:", response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        books = []
        print("Request failed:", e)

    return render(request, 'adminapp/list_books.html', {'books': books})

@login_required(login_url='adminapp:login')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)  # include request.FILES for image/file upload
        if form.is_valid():
            data = form.cleaned_data
            try:
                response = requests.post(
                    'http://127.0.0.1:8000/book/api/Books/',
                    data={
                        'title': data['title'],
                        'author': data['author'],
                        'description': data['description'],
                        'isbn': data['isbn'],
                        'published_date': data['published_date'].isoformat(),  # convert to string
                    },
                    files={
                        'cover_photo': request.FILES.get('cover_photo'),
                        'file': request.FILES.get('file'),
                    }
                )
                if response.status_code == 201:
                    return redirect('adminapp:list_books')  # use your app namespace here
                else:
                    print("API error:", response.status_code, response.text)
            except requests.exceptions.RequestException as e:
                print("Request failed:", e)
    else:
        form = BookForm()

    return render(request, 'adminapp/add_book.html', {'form': form})
@login_required(login_url='adminapp:login')
def edit_book(request, pk):
    # Fetch the book data from your backend API
    try:
        response = requests.get(f'http://127.0.0.1:8000/book/api/Books/{pk}/')
        if response.status_code != 200:
            return render(request, 'adminapp/error.html', {'message': 'Book not found'})
        book_data = response.json()
    except requests.exceptions.RequestException as e:
        return render(request, 'adminapp/error.html', {'message': f'Error: {e}'})

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            files = {}
            if request.FILES.get('cover_photo'):
                files['cover_photo'] = request.FILES['cover_photo']
            if request.FILES.get('file'):
                files['file'] = request.FILES['file']
            try:
                response = requests.put(
                    f'http://127.0.0.1:8000/book/api/Books/{pk}/',
                    data={
                        'title': data['title'],
                        'author': data['author'],
                        'description': data['description'],
                        'isbn': data['isbn'],
                        'published_date': data['published_date'].isoformat(),
                    },
                    files=files if files else None
                )
                if response.status_code in [200, 202]:
                    return redirect('adminapp:list_books')
                else:
                    return render(request, 'adminapp/error.html', {'message': f'Update failed: {response.text}'})
            except requests.exceptions.RequestException as e:
                return render(request, 'adminapp/error.html', {'message': f'Error: {e}'})
    else:
        # Prepopulate the form with the existing data
        form = BookForm(initial={
            'title': book_data['title'],
            'author': book_data['author'],
            'description': book_data['description'],
            'isbn': book_data['isbn'],
            'published_date': book_data['published_date'],
        })

    return render(request, 'adminapp/edit_book.html', {'form': form, 'book_id': pk})

   

@login_required(login_url='adminapp:login')
def delete_book(request, pk):
    if request.method == 'POST':
        try:
            response = requests.delete(f'http://127.0.0.1:8000/book/api/Books/{pk}/')
            if response.status_code in [204, 200]:
                return redirect('adminapp:list_books')
            else:
                return render(request, 'adminapp/error.html', {
                    'message': f'Deletion failed: {response.status_code} - {response.text}'
                })
        except requests.exceptions.RequestException as e:
            return render(request, 'adminapp/error.html', {'message': f'Request failed: {e}'})
    
    # Optional: get book details to show in the confirmation page
    try:
        response = requests.get(f'http://127.0.0.1:8000/book/api/Books/{pk}/')
        if response.status_code == 200:
            book = response.json()
        else:
            book = None
    except requests.exceptions.RequestException:
        book = None

    return render(request, 'adminapp/delete_book.html', {'book': book})

def admin_logout(request):
    logout(request)
    return redirect('adminapp:login')
