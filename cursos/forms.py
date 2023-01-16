from .models import Curso, Modulo, Conteudo
from django import forms


class CursoForm(forms.ModelForm):

	class Meta:
		model = Curso
		fields = ['titulo', 'descricao', 'imagem', 'carga_horaria']


class ModuloForm(forms.ModelForm):

	class Meta:
		model = Modulo
		fields = ['titulo', 'descricao', 'carga_horaria', 'ordem']

class ConteudoForm(forms.ModelForm):

	class Meta:
		model = Conteudo
		fields = ['titulo', 'url_video','descricao', 'ordem']

