from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import RegistroForm

from django.contrib.messages.views import SuccessMessageMixin


class Registro(SuccessMessageMixin, generic.CreateView):
	form_class = RegistroForm
	success_url = reverse_lazy('login')
	template_name = 'registration/register.html'
	success_message = "%(username)s, você foi registrado com sucesso!"