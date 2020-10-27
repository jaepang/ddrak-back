from django.shortcuts import render
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters import rest_framework as filters
from django.db import models as django_models

from .models import Event 
from .serializers import EventSerializer, UserSerializer, UserSerializerWithToken

class MonthlyFilter(filters.FilterSet):
    start__gte = filters.IsoDateTimeFilter(field_name="start", lookup_expr="gte")
    start__lt = filters.IsoDateTimeFilter(field_name="start", lookup_expr="lt")

    class Meta:
        model = Event
        fields = ["start"]

class ListEvent(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_class = MonthlyFilter

class DetailEvent(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

@api_view(['GET'])
def CurrentUser(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
