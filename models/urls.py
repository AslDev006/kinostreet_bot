from django.urls import path, include, register_converter
from .views import *

urlpatterns = [
    path('movies/', MovieListView.as_view()),
    path('movies/create/', MoviesCreateView.as_view()),
    path('movies/<id>/', MoviesDetailView),
    path('films/', FilmsListView),
]