from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, Session


class HomeMovie(ListView):
	model = Session
	template_name = 'movie/session_list.html'
	context_object_name = 'sessions'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Сеанси'
		return context

	def get_queryset(self):
		return Session.objects.order_by('time').all()


class Movies(ListView):
	model = Movie
	template_name = 'movie/movie_list.html'
	context_object_name = 'movies'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Фільми'
		return context

	def get_queryset(self):
		return Movie.objects.all()


class ViewMovie(DetailView):
	model = Movie
	context_object_name = 'movie_item'


class Hall(DetailView):
	model = Session
	context_object_name = 'hall_item'
	template_name = 'movie/hall_detail.html'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Забронювати сеанс'
		context['seats_range'] = range(1, super().get_context_data(**kwargs)['hall_item'].hall.seats + 1)  # take a numer of seats in hall
		return context


# def hall_view(request, time, pk):
# 	session = Session.objects.all()
# 	context={'raws':
#
# 	}
# 	return render(request, 'movie/hall_detail.html')




