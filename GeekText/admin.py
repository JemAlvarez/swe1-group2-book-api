from django.contrib import admin
from .models import Book
from .models import Author
from .models import Publisher
from .models import Genre

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Genre)

# Register your models here.
