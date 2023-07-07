from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from .pagination import CustomPagination

class BookCreateList(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPagination

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSerializer


# Create your views here.
