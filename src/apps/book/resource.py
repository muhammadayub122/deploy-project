from import_export import resources
from .models import Book

class BookResource(resources.ModelResource):
    class Meta:
        model = Book
        # Specify fields to import/export, or use 'fields' or 'exclude'
        fields = ('id', 'name', 'author_name', 'description') 