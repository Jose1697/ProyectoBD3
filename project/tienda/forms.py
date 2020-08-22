from django import forms

from django.contrib.auth.models import User


class SignupForm(forms.Form):
	username = forms.CharField(label=False,min_length=4, max_length=50,
		widget = forms.TextInput(attrs={'placeholder':'Username','class':'form-control','required':True})
	)

	password = forms.CharField(
		label = False,
		max_length=70, 
		widget = forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control','required':True})
	)

	password_confirmation = forms.CharField(
		label = False,
		max_length=70, 
		widget = forms.PasswordInput(attrs={'placeholder':'Password Confirmation','class':'form-control','required':True})
	)

	first_name = forms.CharField(
		label=False,
		min_length=2, 
		max_length=50,
		widget = forms.TextInput(attrs={'placeholder':'First Name','class':'form-control','required':True})
	)

	last_name = forms.CharField(
		label=False,
		min_length=2, 
		max_length=50,
		widget = forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control','required':True})
	)

	email = forms.CharField(
		label=False,
		min_length=6,
		max_length=70,
		widget=forms.EmailInput(attrs={'placeholder':'Email','class':'form-control','required':True}),
		
	)

	def clean_username(self):
		"""Username debe ser unique"""
		username = self.cleaned_data['username']
		username_taken = User.objects.filter(username=username).exists()
		if username_taken:
			raise forms.ValidationError('Username ya esta en uso.')
		return username

	def clean(self):
		"""Verificar la confirmacion de password"""
		data = super().clean()
		password = data['password']
		password_confirmation = data['password_confirmation']

		if password != password_confirmation:
			raise forms.ValidationError("Los passwords no coinciden") #Lanzar una excepcion

		return data

	def save(self):
		"""Crear user"""
		data = self.cleaned_data
		"""Password confirmation no sirve para guardar 
			asi que lo sacamos"""
		data.pop('password_confirmation')
		user = User.objects.create_user(**data)
		