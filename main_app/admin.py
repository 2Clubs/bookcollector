from django.contrib import admin
from .models import Book, Reading, Genre

# Register your models here.
admin.site.register(Book)
admin.site.register(Reading)
admin.site.register(Genre)