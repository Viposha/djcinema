from django.urls import path
from .views import home, Movies, ViewMovie


urlpatterns = [
	path('', home, name='home'),
	path('movies/', Movies.as_view(), name='movies'),
	path('movies/<str:pk>/', ViewMovie.as_view(), name='movie_detail'),

]