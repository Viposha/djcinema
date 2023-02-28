from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator


class CheckoutForm(forms.Form):
	card_number = forms.IntegerField()
	valid_to = forms.CharField(max_length=5)
	cvv = forms.IntegerField()
	email = forms.EmailField()