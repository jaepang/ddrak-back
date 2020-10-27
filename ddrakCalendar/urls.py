from django.urls import path

from .views import *

urlpatterns = [
    path('', ListEvent.as_view()),
    path('<int:pk>/', DetailEvent.as_view()),

    path('current-user/', CurrentUser),
    path('users/', UserList.as_view())
]
