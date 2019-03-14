"""In the code above we specify how to get the objects from the database by setting the queryset attribute of the class and specify a serializer that will be used in serializing and deserializing the data.

The view in this code inherits from a generic viewset ListViewSet . A complete documentation about generic viewsets can be found here for your reference"""

from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from music.models import Songs
from .serializers import SongsSerializer


class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
