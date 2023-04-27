from django.db import models
from django.urls import reverse
from isbn_field import ISBNField

FORMAT = (
    ('E', 'E-Reader'),
    ('H', 'Hard Copy'),
)

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    isbn = ISBNField(clean_isbn=True, max_length=20)
    
    # override __str__ method
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("detail", kwargs={"book_id": self.id})
    
class Reading(models.Model):
    date = models.DateTimeField()
    format = models.CharField(
        max_length=1,
        choices=FORMAT,
        default=FORMAT[0][0],
        )
    notes = models.CharField(max_length=500)
    
    def __str__(self):
        return f"{self.get_format_display() on (self.date)}"
    
# books = [
#     Book('Moby-Dick', 'Herman Melville', 'Penguin Books', 2003),
#     Book('Hard Times', 'Charles Dickens', 'Broadview Press', 2000),
#     Book('To Kill a Mockingbird', 'Harper Lee', 'J.B. Lippincott Company', 1960)
# ]