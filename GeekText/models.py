from django.db import models

# Create your models here...


class Book(models.Model):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=60)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    sold = models.IntegerField(default='0')
    rating = models.FloatField(default='0')
    price = models.FloatField()
    description = models.CharField(max_length=120)
    year = models.IntegerField()
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Author(models.Model):
    fName = models.CharField(max_length=60)
    lName = models.CharField(max_length=60, primary_key=True)
    bio = models.CharField(max_length=120)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)

    def __str__(self):

        return self.fName + " " + self.lName


class Publisher(models.Model):
    name = models.CharField(max_length=60, primary_key=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(primary_key=True, max_length=60)

    def __str__(self):
        return self.name

