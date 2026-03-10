from django.contrib import admin
from .models import Book
from import_export.admin import ImportExportModelAdmin
from .resource import BookResource
# Register your models here.

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    # Optional: configure the resource class if you need customization
    resource_classes = [BookResource] 
    list_display = ['name', 'author_name']