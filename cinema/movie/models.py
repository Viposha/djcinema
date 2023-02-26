from django.db import models


class Hall(models.Model):
	title = models.CharField(max_length=100, primary_key=True)
	seats = models.IntegerField()
	rows = models.IntegerField()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Зал'
		verbose_name_plural = 'Зали'



class Movie(models.Model):
	title = models.CharField(max_length=100, primary_key=True)
	description = models.TextField()
	genre = models.CharField(max_length=50)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Фільм'
		verbose_name_plural = 'Фільми'



class Review(models.Model):
	rating = models.IntegerField()
	content = models.TextField()
	title = models.ForeignKey(Movie, on_delete=models.PROTECT)

	def __str__(self):
		return self.content

	class Meta:
		verbose_name = 'Відгук'
		verbose_name_plural = 'Відгуки'



class Session(models.Model):
	hall = models.ForeignKey(Hall, on_delete=models.PROTECT)
	title = models.ForeignKey(Movie, on_delete=models.PROTECT)
	time = models.CharField(max_length=100)
	date = models.CharField(max_length=100)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Сеанс'
		verbose_name_plural = 'Сеанси'



class Ticket(models.Model):
	raw = models.IntegerField()
	seat = models.IntegerField()
	hall = models.ForeignKey(Hall, on_delete=models.PROTECT)
	title = models.ForeignKey(Movie, on_delete=models.PROTECT)
	time = models.CharField(max_length=10)
	user_email = models.EmailField(max_length=50, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Квиток'
		verbose_name_plural = 'Квитки'
		ordering = ['id']


