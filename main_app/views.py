from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hello')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    return render(request, 'books/index.html', { 'books': books })