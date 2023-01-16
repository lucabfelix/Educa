from django.contrib import admin

from .models import Curso, Modulo, Conteudo, Inscricao

admin.site.register(Curso)
admin.site.register(Modulo)
admin.site.register(Conteudo)
admin.site.register(Inscricao)



