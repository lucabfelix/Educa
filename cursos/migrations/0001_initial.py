# Generated by Django 4.1.4 on 2022-12-20 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, verbose_name='Título')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('imagem', models.ImageField(upload_to='', verbose_name='Imagem do Curso')),
                ('carga_horaria', models.CharField(max_length=50, verbose_name='Carga Horária')),
                ('dt_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('dt_alteracao', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursos_criados', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, verbose_name='Título')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('carga_horaria', models.CharField(max_length=50, verbose_name='Carga Horária')),
                ('ordem', models.PositiveIntegerField(blank=True, default=0, verbose_name='Número (ordem)')),
                ('dt_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('dt_alteracao', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modulos', to='cursos.curso')),
            ],
            options={
                'verbose_name': 'Módulo',
                'verbose_name_plural': 'Módulos',
                'ordering': ['ordem'],
            },
        ),
        migrations.CreateModel(
            name='Conteudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, verbose_name='Título')),
                ('url_video', embed_video.fields.EmbedVideoField()),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('ordem', models.PositiveIntegerField(blank=True, default=0, verbose_name='Número (ordem)')),
                ('dt_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('dt_alteracao', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conteudos', to='cursos.modulo')),
            ],
            options={
                'verbose_name': 'Conteúdo',
                'verbose_name_plural': 'Conteúdos',
                'ordering': ['ordem'],
            },
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')], default=1, verbose_name='Situação')),
                ('dt_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('dt_alteracao', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscricao', to='cursos.curso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscricao', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Inscrição',
                'verbose_name_plural': 'Inscrições',
                'unique_together': {('usuario', 'curso')},
            },
        ),
    ]