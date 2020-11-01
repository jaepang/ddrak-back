from django.shortcuts import render
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters import rest_framework as filters
from django.db import models as django_models
from django.contrib.auth.models import User

from .models import Event 
from .serializers import *

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
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class UserList(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(generics.UpdateAPIView):
        serializer_class = ChangePasswordSerializer
        model = User

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
