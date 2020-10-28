from django.urls import path
from . import controller

urlpatterns = [
    path('', controller.View, name = 'home-page'),
    path('navigate_to_movie', controller.navigate_to_movie, name = 'navigate_to_movie'),
]