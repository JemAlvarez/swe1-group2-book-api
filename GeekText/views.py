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


# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Book.objects.all()
        genre = self.request.query_params.get('genre')
        if genre is not None:
            queryset = queryset.filter(genre=genre)
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
