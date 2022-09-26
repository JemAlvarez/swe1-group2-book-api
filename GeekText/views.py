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

        queryset = Book.objects.all()

        genre_val = self.request.query_params.get('genre')
        top_val = self.request.query_params.get('top')
        rating_val = self.request.query_params.get('min_rating')
        retrieve_qty = self.request.query_params.get('retrieve')
        start_pos = self.request.query_params.get('startpos')

        if genre_val is not None:
            queryset = queryset.filter(genre=genre_val)

        if top_val is not None:
            if top_val == "":
                top_val = 10
            queryset = queryset.order_by('-sold')[:int(top_val)]

        if rating_val is not None:
            print("min rating" + rating_val)
            queryset = queryset.filter(rating__gte=float(rating_val))

        if retrieve_qty is not None:
            if start_pos is None:
                start_pos = "0"

            end_pos = int(start_pos) + int(retrieve_qty) - 1
            print("retrieve qty " + retrieve_qty)
            print("start pos " + start_pos)

            queryset = queryset.filter(id__range=(int(start_pos), end_pos))

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
