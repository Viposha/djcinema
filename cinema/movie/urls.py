from django.urls import path
from .views import Movies, ViewMovie, HomeMovie


urlpatterns = [
	path('', HomeMovie.as_view(), name='home'),
	path('movies/', Movies.as_view(), name='movies'),
	path('movies/<str:pk>/', ViewMovie.as_view(), name='movie_detail'),
	]