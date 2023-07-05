from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
