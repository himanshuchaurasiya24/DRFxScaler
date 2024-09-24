from home.views import *
from django.urls import path, include
from rest_framework.views import APIView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'persons', PersonViewSet, basename='people')

urlpatterns = [
    path('index/', index),
    # path('/', index),
    # path('login/', login),
    path('login/', LoginAPI.as_view()),
    # path('person/', person),
    path('register/', RegisterAPI.as_view()),
    path('persons/', PersonAPI.as_view()),
    path('',include(router.urls)),
]
