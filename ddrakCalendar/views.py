from django.shortcuts import render
from rest_framework import permissions, generics

from .models import Event 
from .serializers import EventSerializer

class ListEvent(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class DetailEvent(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

