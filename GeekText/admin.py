from django.contrib import admin
from .models import Book
from .models import Author
from .models import Publisher
from .models import Genre
from .models import Wishlist
from .models import RatingBooks

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Wishlist)
admin.site.register(RatingBooks)


# Register your models here.
