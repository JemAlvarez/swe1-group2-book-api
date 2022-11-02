from django.contrib import admin
from .models import Book
from .models import Author
from .models import Publisher
from .models import Genre
from .models import Wishlist

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Wishlist)

# Register your models here.
