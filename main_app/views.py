from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book, Genre
from .forms import ReadingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', { 'books': books })

def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    reading_form = ReadingForm()
    genres_book_doesnt_have = Genre.objects.exclude(id__in = book.genre.all().values_list('id'))
    return render(request, 'books/detail.html', { 'book': book, 'reading_form': reading_form, 'genres': genres_book_doesnt_have })

def add_reading(request, book_id):
    form = ReadingForm(request.POST)
    if form.is_valid():
        new_reading = form.save(commit=False)
        new_reading.book_id = book_id
        new_reading.save()
    return redirect('detail', book_id=book_id)
  
def assoc_genre(request, book_id, genre_id):
    Book.objects.get(id=book_id).genre.add(genre_id)
    return redirect('detail', book_id=book_id)

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    
class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    
class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'
    
class GenreIndex(ListView):
  model = Genre

class GenreDetail(DetailView):
  model = Genre
  
class GenreCreate(CreateView):
  model = Genre
  fields = '__all__'

class GenreUpdate(UpdateView):
  model = Genre
  fields = '__all__'

class GenreDelete(DeleteView):
  model = Genre
  success_url = '/genre/'