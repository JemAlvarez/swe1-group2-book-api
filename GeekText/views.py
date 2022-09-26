from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .serializers import AuthorSerializer
from .serializers import PublisherSerializer
from .serializers import GenreSerializer
from .models import Book
from .models import Author
from .models import Publisher
from .models import Genre
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def getBookByISBN(request, isbn, *args, **kwargs):
    books = Book.objects.filter(isbn=isbn)
    
    if not books:
        return Response({"error": "No book found with the given ISBN"})
    else:
        return Response(BookSerializer(
            books[0]
        ).data)

@api_view(['GET'])
def getAuthorBooks(request, name, *args, **kwargs):
    author_name = name.split("+")
    author_objs = Author.objects.filter(fName=author_name[0], lName=author_name[1])
    all_books = Book.objects.all()
    author_books = []

    for book in all_books:
        if book.author == author_objs[0]:
            author_books.append(book)
            
    return Response(BookSerializer(
        author_books,
        many=True
    ).data)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """

        queryset = Book.objects.all()
        genre_val = self.request.query_params.get('genre')
        top_val = self.request.query_params.get('top')
        rating_val = self.request.query_params.get('min_rating')

        if genre_val is not None:
            queryset = queryset.filter(genre=genre_val)

        if top_val is not None:
            if top_val == "":
                top_val = 10
            queryset = queryset.order_by('-sold')[:int(top_val)]

        if rating_val is not None:
            print("min rating" + rating_val)
            #queryset = queryset.filter(genre=genre_val)
            queryset = queryset.filter(rating__gte=float(rating_val))

        return queryset


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('fName')
    serializer_class = AuthorSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all().order_by('name')
    serializer_class = PublisherSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
