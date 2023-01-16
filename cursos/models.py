from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


class Curso(models.Model):
    usuario = models.ForeignKey(User, related_name='cursos_criados', 
                                        on_delete=models.CASCADE, verbose_name='Usuário')
    titulo = models.CharField('Título', max_length=150)
    descricao = models.TextField('Descrição')
    imagem = models.ImageField('Imagem do Curso')
    carga_horaria = models.CharField('Carga Horária', max_length=50)
    dt_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    dt_alteracao = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.titulo

class Modulo(models.Model):
    curso = models.ForeignKey(Curso, related_name='modulos',
                               on_delete=models.CASCADE)
    titulo = models.CharField('Título', max_length=150)
    descricao = models.TextField('Descrição')
    carga_horaria = models.CharField('Carga Horária', max_length=50)
    ordem = models.PositiveIntegerField('Número (ordem)', blank=True, default=0)
    dt_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    dt_alteracao = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Módulo'
        verbose_name_plural = 'Módulos'
        ordering = ["ordem"]

class Conteudo(models.Model):
    modulo = models.ForeignKey(Modulo, related_name='conteudos',
                               on_delete=models.CASCADE)
    titulo = models.CharField('Título', max_length=150)
    url_video = EmbedVideoField()
    descricao = models.TextField('Descrição')
    ordem = models.PositiveIntegerField('Número (ordem)', blank=True, default=0)
    dt_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    dt_alteracao = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.titulo

    def proxima_aula(self):
        return Conteudo.objects.filter(modulo__curso=self.modulo.curso, 
            ordem__gt=self.ordem).order_by('ordem').first()

    def aula_anterior(self):
        return Conteudo.objects.filter(modulo__curso=self.modulo.curso, 
            ordem__lt=self.ordem).order_by('-ordem').first()

    class Meta:
        verbose_name = 'Conteúdo'
        verbose_name_plural = 'Conteúdos'
        ordering = ["ordem"]

class Inscricao(models.Model):
    STATUS_CHOICES = (
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Cancelado'),
    )
    usuario = models.ForeignKey(User, related_name='inscricao', 
                                        on_delete=models.CASCADE, verbose_name='Usuário')
    curso = models.ForeignKey(Curso, related_name='inscricao',
                               on_delete=models.CASCADE)
    status = models.IntegerField(
        'Situação', choices=STATUS_CHOICES, default=1, blank=True)

    dt_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    dt_alteracao = models.DateTimeField('Atualizado em', auto_now=True)

    def active(self):
        self.status = 1
        self.save()

    def is_approved(self):
        return self.status == 1

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = (('usuario', 'curso'),)
