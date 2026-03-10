from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255, default="Bobur Mirzo")   
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name