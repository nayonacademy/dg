from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
            return str(self.title)


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField()

    def __str__(self):
            return str(self.first_name)


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)