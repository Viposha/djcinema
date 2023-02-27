from django.shortcuts import render
from django.views.generic import ListView
from .models import Movie


def home(request):
	return render (request, 'movie/home.html')


class Movies(ListView):
	model = Movie
	template_name = 'movie/movie_list.html'
	context_object_name = 'movies'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

	def get_queryset(self):
		return Movie.objects.all()