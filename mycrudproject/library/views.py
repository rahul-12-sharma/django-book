from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm, SignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')  

# SIGN UP
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book-list')  # Redirect to book list after signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# LOGIN
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book-list')  # Redirect to book list after login
    else:
        form = AuthenticationForm()
    return render(request, 'logIn.html', {'form': form})

# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login after logout


# Create Book
@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')  # Redirect to book list after saving the book
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


# Read 
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


# Update Book 
@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')  # Redirect to book list after editing the book
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})


# Delete Book 
@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')  # Redirect to book list after deleting the book
    return render(request, 'delete_book.html', {'book': book})
