from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class RegistroForm(UserCreationForm):
	email = forms.EmailField(label="E-mail", help_text='Obrigatório.')
	first_name = forms.CharField(label="Nome Completo", max_length=150, help_text='Obrigatório. 150 caracteres ou menos. ')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email', 'password1', 'password2')

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("Já existe um usuário com este email cadastrado!")
		return email
		