from django.db import models
from isbn_field import ISBNField

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    isbn = ISBNField(clean_isbn=True, max_length=20)
    
    # override __str__ method
    def __str__(self):
        return self.title
        
# books = [
#     Book('Moby-Dick', 'Herman Melville', 'Penguin Books', 2003),
#     Book('Hard Times', 'Charles Dickens', 'Broadview Press', 2000),
#     Book('To Kill a Mockingbird', 'Harper Lee', 'J.B. Lippincott Company', 1960)
# ]