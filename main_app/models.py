from django.db import models

# Create your models here.
class Book:
    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        
books = [
    Book('Moby-Dick', 'Herman Melville', 'Penguin Books', 2003),
    Book('Hard Times', 'Charles Dickens', 'Broadview Press', 2000),
    Book('To Kill a Mockingbird', 'Harper Lee', 'J.B. Lippincott Company', 1960)
]