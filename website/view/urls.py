from django.urls import path
from . import Controller

urlpatterns = [
    path('', Controller.View, name = 'home-page'),
]