from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from apps.forms import *
from apps.models import *

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'apps/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            # Return an 'invalid login' error message.
            return HttpResponseRedirect(reverse('index'))


def dashboard(request):
    author_count = Author.objects.count()
    book_cout = Book.objects.count()
    context = {
        'author' : author_count,
        'book' : book_cout,
    }
    return render(request, 'apps/dashboard.html', context)


def addBooks(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return HttpResponseRedirect(reverse('dashboard'))
    else:

        form = BookForm()
        return render(request, 'apps/add_books.html',{'form': form}) 


def allBooks(request):
    books_list = Book.objects.all()
    return render(request, 'apps/all_books.html',{'books_list':books_list})


def book_details(request, id):
    books_list = Book.objects.filter(id=id)
    return render(request, 'apps/book_details.html',{'books_list':books_list})


def allAuthors(request):
    author_list = Author.objects.all()
    return render(request, 'apps/all_authors.html',{"author_list":author_list})


def author_details(request, id):
    author_list = Author.objects.filter(id=id)
    return render(request, 'apps/author_details.html',{'author_list':author_list})


def addAuthor(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return HttpResponseRedirect(reverse('dashboard'))
    else:

        form = AuthorForm()
        return render(request, 'apps/add_author.html',{'form': form}) 


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))