from .views import *
from django.urls import path

urlpatterns = [
    path('', FilmsList.as_view(), name='films'),
    path('update_films/', update_films, name='update_films')
]
