from re import M
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .serializers import AuthorSerializer
from .serializers import PublisherSerializer
from .serializers import GenreSerializer
from .serializers import WishlistSerializer
from .serializers import RatingBooksSerializers
from .serializers import UserSerializer
from .models import Book
from .models import Author
from .models import Publisher
from .models import Genre
from .models import Wishlist
from .models import RatingBooks
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import permissions
import json
from itertools import chain
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@api_view(['GET'])
def getAllWishLists(request, user, *args, **kwargs):
    wishlist = Wishlist.objects.filter(owner_id=user)

    if not wishlist:
        return Response({"error": "No wishlist found for given user."})
    else:
        return Response(WishlistSerializer(wishlist, many=True).data)


@api_view(['GET', 'DELETE', 'POST'])
def wishlist(request, user, wishlist_name, *args, **kwargs):
    if request.method == 'GET':
        wishlist = Wishlist.objects.filter(
            owner_id=user, wishlist_name=wishlist_name)

        if not wishlist:
            return Response({"error": "No wishlist found for given user."})
        else:
            return Response(WishlistSerializer(wishlist, many=True).data)
    elif request.method == 'POST':
        body = json.loads(request.body)
        books = Wishlist.objects.create(
            wishlist_name=wishlist_name, books_id=body["book_id"], owner_id=user)
        books.save()

        return Response(WishlistSerializer(books).data, status=201)
    elif request.method == 'DELETE':
        body = json.loads(request.body)
        books = Wishlist.objects.filter(
            wishlist_name=wishlist_name, books_id=body["book_id"], owner_id=user)
        books.delete()

        return Response({"message": "Successfully deleted book in wishlist"}, status=200)


@ api_view(['GET'])
def getBookByISBN(request, isbn, *args, **kwargs):
    books = Book.objects.filter(isbn=isbn)

    if not books:
        return Response({"error": "No book found with the given ISBN"})
    else:
        return Response(BookSerializer(books[0]).data)


@ api_view(['GET'])
def getAuthorBooks(request, name, *args, **kwargs):
    author_name = name.split("+")
    author_objs = Author.objects.filter(fName=author_name[0],
                                        lName=author_name[1])
    all_books = Book.objects.all()
    author_books = []

    for book in all_books:
        if book.author == author_objs[0]:
            author_books.append(book)

    return Response(BookSerializer(author_books, many=True).data)


@ api_view(['GET', 'POST'])
@ permission_classes([permissions.IsAuthenticatedOrReadOnly])
def book(request):
    if request.method == 'GET':
        queryset = Book.objects.all()
        genre_val = request.query_params.get('genre')
        top_val = request.query_params.get('top')
        rating_val = request.query_params.get('min_rating')
        retrieve_qty = request.query_params.get('retrieve')
        start_pos = request.query_params.get('startpos')

        if genre_val is not None:
            queryset = queryset.filter(genre=genre_val)

        if top_val is not None:
            if top_val == "":
                top_val = 10
            queryset = queryset.order_by('-sold')[:int(top_val)]

        if rating_val is not None:
            queryset = queryset.filter(
                rating__gte=float(rating_val)).order_by('-rating')

        if retrieve_qty is not None:
            if start_pos is None:
                start_pos = "1"
            end_pos = int(start_pos) + int(retrieve_qty) - 1
            queryset = queryset.filter(id__range=(int(start_pos), end_pos))

        return Response(BookSerializer(queryset, many=True).data)

    elif request.method == 'POST':
        body = json.loads(request.body)
        publisher = Publisher.objects.filter(name=body['publisher'])
        genre = Genre.objects.filter(name=body['genre'])
        author = Author.objects.filter(lName=body['author'])

        if publisher.exists() & genre.exists() & author.exists():
            book = Book(isbn=body['isbn'],
                        title=body['title'],
                        genre=genre[0],
                        sold=body['sold'],
                        rating=body['rating'],
                        price=body['price'],
                        description=body['description'],
                        year=body['year'],
                        publisher=publisher[0],
                        author=author[0])
            book.save()
            return Response(BookSerializer(book).data, status=201)
        else:
            return Response({"error": "Invalid publisher, author, or genre"},
                            status=400)


@ api_view(['GET', 'POST'])
@ permission_classes([permissions.IsAuthenticatedOrReadOnly])
def author(request):
    if request.method == 'GET':
        return Response(
            AuthorSerializer(Author.objects.all().order_by('fName'),
                             many=True).data)
    elif request.method == 'POST':
        body = json.loads(request.body)
        publisher = Publisher.objects.filter(name=body['publisher'])

        if publisher:
            author = Author(fName=body['fName'],
                            lName=body['lName'],
                            bio=body['bio'],
                            publisher=publisher[0])
            author.save()
            return Response(AuthorSerializer(author).data, status=201)
        else:
            return Response({"error": "Publish does not exist"}, status=400)


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all().order_by('name')
    serializer_class = PublisherSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
    
    # Create your views here.

class RatingViewSets(viewsets.ModelViewSet):
    queryset = RatingBooks.objects.all()
    serializer_class = RatingBooksSerializers    


class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
