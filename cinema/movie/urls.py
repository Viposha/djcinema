from django.urls import path
from .views import Movies, ViewMovie, HomeMovie, Hall


urlpatterns = [
	path('', HomeMovie.as_view(), name='home'),
	path('movies/', Movies.as_view(), name='movies'),
	path('movies/<str:pk>/', ViewMovie.as_view(), name='movie_detail'),
	path('<str:pk>/<str:time>/', Hall.as_view(), name='hall'),
	]