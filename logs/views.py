from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'logs/book_list.html', {'book_list': books})
# Create your views here.
