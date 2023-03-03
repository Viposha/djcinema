from django import forms
from django.core.exceptions import ValidationError
from .models import Review
from captcha.fields import CaptchaField
import re


class ReviewForm(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = Review
		fields = ['rating', 'content', 'title']
		labels = {
			'rating': 'Рейтинг',
			'content': 'Відгук',
			'title': 'Обери фільм',
			'captcha': 'Виріши приклад'
		}
		widgets = {
		'rating': forms.Select(attrs={'class': 'form-control'}),
		'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
		'title': forms.Select(attrs={'class': 'form-control'})
		}


class CheckoutForm(forms.Form):
	card_number = forms.IntegerField(label='Номер картки', widget=forms.NumberInput(attrs={'class':'form-control'}))
	valid_to = forms.CharField(label='Термін дії  mm/yy', widget=forms.TextInput(attrs={'class':'form-control'}))
	cvv = forms.IntegerField( widget=forms.NumberInput(attrs={'class':'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

	def clean_card_number(self):
		card_number = self.cleaned_data['card_number']
		if len(str(card_number)) != 16:
			raise ValidationError(f'Номер картки має містити 16 символів. Ви ввели {len(str(card_number))}')
		return card_number

	def clean_cvv(self):
		cvv = self.cleaned_data['cvv']
		if len(str(cvv)) != 3:
			raise ValidationError('Поле Cvv має містити 3 символа')
		return cvv

	def clean_valid_to(self):
		valid_to = self.cleaned_data['valid_to']
		if not re.match(r"\d{2}/\d{2}", valid_to):
			raise ValidationError('Поле Термін дії має виглядати так mm/yy')
		elif int(valid_to[0:2]) > 12 or int(valid_to[0:2]) < 1:
			raise ValidationError('Поле mm має бути від 1 до 12')
		return valid_to
