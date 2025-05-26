from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializers
from .models import Book
# Create your views here.

class BookApiView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
