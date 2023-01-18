from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import api_home

urlpatterns = [
    path('', api_home),
]