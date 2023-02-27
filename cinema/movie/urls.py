from django.urls import path
from .views import home, Movies


urlpatterns = [
	path('', home, name='home'),
	path('movies/', Movies.as_view(), name='movies')
]