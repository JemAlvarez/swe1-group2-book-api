# serializers.py
from rest_framework import serializers

from .models import Book
from .models import Author
from .models import Genre
from .models import Publisher
from .models import RatingBooks


class WishlistSerializer(serializers.ModelSerializer):
    wishlistBooks = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Book.objects.all())

    class Meta:
        model = Book
        fields = ('isbn', 'title', 'author', 'genre', 'publisher', 'year',
                  'description', 'price', 'sold', 'rating', 'id')


class BookSerializer(serializers.ModelSerializer):

    genre = serializers.PrimaryKeyRelatedField(many=False,
                                               queryset=Genre.objects.all())

    author = serializers.PrimaryKeyRelatedField(many=False,
                                                queryset=Author.objects.all())

    publisher = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Publisher.objects.all())

    class Meta:
        model = Book
        fields = ('isbn', 'title', 'author', 'genre', 'publisher', 'year',
                  'description', 'price', 'sold', 'rating', 'id')
        #fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    publisher = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Publisher.objects.all())

    class Meta:
        model = Author
        fields = ('fName', 'lName', 'bio', 'publisher')


class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

 class RatingBooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = RatingBooks
        fields = '__all__'
