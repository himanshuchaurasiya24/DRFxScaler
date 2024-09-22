from home.views import *
from django.urls import path
from rest_framework.views import APIView
urlpatterns = [
    path('index/', index),
    path('/', index),
    path('login/', login),
    path('person/', person),
    path('persons/', PersonAPI.as_view())
]
