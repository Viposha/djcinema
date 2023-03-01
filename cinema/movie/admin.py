from django.contrib import admin

from .models import Movie, Session, Ticket, Hall, Review


class HallAdmin(admin.ModelAdmin):
	list_display = ('title', 'seats', 'rows')
	list_display_links = ('title',)


class MovieAdmin(admin.ModelAdmin):
	list_display = ('title', 'genre', 'photo')
	list_display_links = ('title',)


class SessionAdmin(admin.ModelAdmin):
	list_display = ('hall', 'title', 'price', 'time', 'date')
	list_display_links = ('title',)
	ordering = ('time',)


class TicketAdmin(admin.ModelAdmin):
	list_display = ('seat_id', 'row', 'seat', 'hall', 'title', 'time', 'user_email')
	list_display_links = ('title', 'user_email')


admin.site.register(Hall, HallAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Ticket, TicketAdmin)