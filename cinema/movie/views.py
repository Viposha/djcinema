from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Movie, Session, Ticket, Review
from .forms import CheckoutForm, ReviewForm
from .utils import seats_dict


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

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['movie_title'] = super().get_context_data(**kwargs)['movie_item']
		context['form'] = ReviewForm()
		context['review'] = Review.objects.all()
		return context

	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			form = ReviewForm(request.POST)
			review = form.save()
			return redirect(reverse('home'))


class Hall(DetailView):
	model = Session
	context_object_name = 'hall_item'
	template_name = 'movie/hall_detail.html'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Забронювати сеанс'
		context['seats_range'] = range(1, super().get_context_data(**kwargs)['hall_item'].hall.seats + 1)  # take a number of seats in hall
		tickets= Ticket.objects.filter(time=context['hall_item'].time)
		seats_id_list = []
		for ticket in tickets:
			seats_id_list.append(ticket.seat_id)
		context['seats_id_list'] = seats_id_list
		return context

	def post(self, request, time, *args, **kwargs):
		if request.method == 'POST':
			picked_seats = request.POST.getlist('seat')
			request.session['data'] = picked_seats
			request.session['time'] = time
			return redirect(reverse('pay'))


def pay_view(request):
	if request.method == 'POST':
		form = CheckoutForm(request.POST)
		form_data = request.POST
		time = request.session.get('time')
		movie = Session.objects.get(time=time)
		email = form_data['email']
		data = request.session.get('data')
		hall = movie.hall.title
		title = movie.title
		if form.is_valid():
			print(form.cleaned_data)
			for place in data:
				seat = seats_dict[int(place)][1]
				row = seats_dict[int(place)][0]
				ticket = Ticket(seat_id=int(place), row=int(row), seat=int(seat), hall_id=hall, title_id=title, time=time, user_email=email)
				ticket.save()
			messages.add_message(request, messages.SUCCESS, 'Квитки придбані. Чекаємо Вас у нашому кінотеатрі!')
			return redirect(reverse('home'))
	else:
		data = request.session.get('data')
		time = request.session.get('time')
		movie = Session.objects.get(time=time)
		total_price = len(data) * movie.price
		form = CheckoutForm()
	return render(request, 'movie/pay.html', {'form': form, 'time': time, 'data': data, 'movie': movie, 'total_price':total_price})