from django.db import models
from django.urls import reverse
# ISBNField functionality found here: https://github.com/secnot/django-isbn-field
from isbn_field import ISBNField
from django.contrib.auth.models import User

FORMAT = (
    ('H', 'Hard Copy'),
    ('E', 'E-Reader'),
)

class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
        
    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("genre_detail", kwargs={"pk": self.id})
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    isbn = ISBNField(clean_isbn=True, max_length=20)
    
    genre = models.ManyToManyField(Genre)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # override __str__ method
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("detail", kwargs={"book_id": self.id})
    
class Reading(models.Model):
    date = models.DateField('reading date')
    format = models.CharField(
        max_length=1,
        choices=FORMAT,
        default=FORMAT[0][0],
        )
    notes = models.CharField(max_length=500)
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_format_display()} on {(self.date)}"
    
    class Meta:
        ordering = ['-date']
    
# books = [
#     Book('Moby-Dick', 'Herman Melville', 'Penguin Books', 2003),
#     Book('Hard Times', 'Charles Dickens', 'Broadview Press', 2000),
#     Book('To Kill a Mockingbird', 'Harper Lee', 'J.B. Lippincott Company', 1960)
# ]