# serializers.py
from rest_framework import serializers

from .models import Book
from .models import Author
from .models import Genre
from .models import Publisher


class BookSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(many=False)
    genre = serializers.StringRelatedField(many=False)
    publisher = serializers.StringRelatedField(many=False)

    class Meta:
        model = Book
        fields = ('isbn', 'title', 'author', 'genre', 'publisher', 'year', 'description', 'price', 'sold', 'rating', )
        #fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('fName', 'lName', 'bio')


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
