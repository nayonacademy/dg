from django.forms import ModelForm
from apps.models import *


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description']


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'notes']


class AuthorBookForm(ModelForm):
    class Meta:
        model = BookAuthor
        fields = '__all__'