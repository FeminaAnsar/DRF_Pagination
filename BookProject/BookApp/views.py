from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book

class BookCreateList(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSerializer


# Create your views here.
