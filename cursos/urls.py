
from django.urls import path

from . import views

urlpatterns = [
    path('cursos/', views.curso, name='cursos'), 
    path('painel/', views.area_restrita, name='area_restrita'),  
    path('admusuario/', views.area_restrita_usuarios, name='area_restrita_usuarios'),  
    path('<int:pk>/adm2', views.area_restrita_modulos, name='area_restrita_modulos'),  
    path('<int:pk>/conteudo', views.area_restrita_conteudos, name='area_restrita_conteudos'),  
    path('<int:pk>/inscricao', views.inscricao, name='inscricao'), 
    path('adicionar/', views.adicionar_curso, name='adicionar_curso'),
    path('<int:id>/modulo', views.adicionar_modulo, name='adicionar_modulo'),
 	path('deletar_curso/<str:pk>/', views.deletar_curso, name="deletar_curso"),
    path('deletar_conteudo/<str:pk>/', views.deletar_conteudo, name="deletar_conteudo"),
    path('deletar_modulo/<str:pk>/', views.deletar_modulo, name="deletar_modulo"),
 	path('editar/<int:id>', views.editar_curso, name='editar_curso'),
    path('editarmodulo/<int:id>', views.editar_modulo, name='editar_modulo'),
    path('editarconteudo/<int:id>', views.editar_conteudo, name='editar_conteudo'),
    path('<int:pk>/detalhe', views.detalhe_curso, name='detalhe_curso'),
    path('<int:id>/novo_conteudo', views.adicionar_conteudo, name='adicionar_conteudo'),
    path('aula/<int:pk>', views.detalhe_aula, name='detalhe_aula'),

 
]

