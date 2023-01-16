from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Curso, Modulo, Inscricao, Conteudo
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import CursoForm, ModuloForm, ConteudoForm


@login_required
def curso(request):
	dados = Curso.objects.order_by("titulo").all()

	return render(request, 'cursos.html', {'dados': dados})

@login_required
def detalhe_curso(request, pk):
	curso = get_object_or_404(Curso, pk=pk)
	modulo_curso = Modulo.objects.filter(curso=curso)
	context = {
		'curso': curso,
		'modulos': modulo_curso,
	}
	return render(request, 'pagina_curso.html', context)


@login_required
def detalhe_aula(request, pk):
	conteudo = get_object_or_404(Conteudo, pk=pk)
	modulo = conteudo.modulo
	curso = modulo.curso
	modulos = Modulo.objects.filter(curso=modulo.curso)
	context = {
        'modulos': modulos,
		'conteudo': conteudo,
		'curso': curso,
	}
	return render(request, 'pagina_aula.html', context)

@login_required
def area_restrita(request):
	curso = Curso.objects.all()

	p = Paginator(Curso.objects.all(), 10)
	page = request.GET.get('page')
	cursos = p.get_page(page)
	nums = "a" * cursos.paginator.num_pages
	return render(request, 'base_admin.html', {'curso': curso, 'cursos': cursos,
		'nums':nums})

@login_required
def area_restrita_usuarios(request):

	usuarios = Inscricao.objects.all()

	p = Paginator(User.objects.all(), 10)
	page = request.GET.get('page')
	modulos = p.get_page(page)
	nums = "a" * modulos.paginator.num_pages

	context = {
		'usuarios': usuarios,
		'nums':nums,
	}
	return render(request, 'base_admin_usuario.html', context)


@login_required
def area_restrita_modulos(request, pk):
	curso = get_object_or_404(Curso, pk=pk)
	modulo_curso = Modulo.objects.filter(curso=curso)

	p = Paginator(User.objects.all(), 10)
	page = request.GET.get('page')
	modulos = p.get_page(page)
	nums = "a" * modulos.paginator.num_pages

	context = {
		'modulos': modulos,
		'curso': curso,
		'modulos': modulo_curso,
		'nums':nums,
	}
	return render(request, 'base_admin_modulo.html', context)

@login_required
def area_restrita_conteudos(request, pk):
	modulo = get_object_or_404(Modulo, pk=pk)
	conteudo = Conteudo.objects.filter(modulo=modulo)
	curso = modulo.curso
	p = Paginator(Conteudo.objects.all(), 10)
	page = request.GET.get('page')
	conteudos = p.get_page(page)
	nums = "a" * conteudos.paginator.num_pages

	context = {
		'conteudo': conteudo,
		'modulo': modulo,
		'conteudos': conteudos,
		'nums':nums,
		'curso': curso,
	}
	return render(request, 'base_admin_conteudo.html', context)

@login_required
def adicionar_curso(request):
	if request.method == 'POST':
		form = CursoForm(request.POST, request.FILES)
		if form.is_valid():
			curso = form.save(commit=False)
			curso.usuario = request.user
			curso.save()
			messages.success(request, 'Curso cadastrado com sucesso!')
			proxima = request.GET.get("proxima")
			if not proxima:
				proxima = "cursos"
			return redirect(proxima)
	else:
		form = CursoForm()
		return render(request, 'cadastro_curso.html', {'form': form})


@login_required
def inscricao(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    inscricao, criado = Inscricao.objects.get_or_create(
        usuario=request.user, curso=curso)
    if criado:
        messages.success(request, 'Você foi inscrito com sucesso!')
        return redirect('detalhe_curso', curso.pk)
    else:
        messages.info(request, 'Você já se inscreveu neste curso!')

    return redirect('cursos')

@login_required
def adicionar_modulo(request, id):
	if request.method == 'POST':
		form = ModuloForm(request.POST, request.FILES)
		curso = get_object_or_404(Curso, pk=id)
		if form.is_valid():
			modulo = form.save(commit=False)
			modulo.usuario = request.user
			modulo.curso = curso
			modulo.save()
			messages.success(request, 'Modulo cadastrado com sucesso!')
			proxima = request.GET.get("proxima")
			if not proxima:
				proxima = "detalhe_curso"
			return redirect(proxima, curso.id)
	else:
		form = ModuloForm()
		curso = get_object_or_404(Curso, pk=id)
		context = {
			'form': form,
			'curso': curso,
		}
		return render(request, 'cadastro_modulo.html', context)

@login_required
def adicionar_conteudo(request, id):
	if request.method == 'POST':
		form = ConteudoForm(request.POST, request.FILES)
		modulo = get_object_or_404(Modulo, pk=id)
		if form.is_valid():
			curso = modulo.curso
			conteudo = form.save(commit=False)
			conteudo.usuario = request.user
			conteudo.modulo = modulo
			conteudo.save()
			messages.success(request, 'Conteúdo cadastrado com sucesso!')
			proxima = request.GET.get("proxima")
			if not proxima:
				proxima = "detalhe_curso"
			return redirect(proxima, curso.id)
	else:
		form = ConteudoForm()
		modulo = get_object_or_404(Modulo, pk=id)
	context = {
		'form': form,
		'modulo': modulo,
	}
	return render(request, 'cadastro_conteudo.html', context)

@login_required
def adicionar_anuncio(request, id):
	if request.method == 'POST':
		form = AnuncioForm(request.POST, request.FILES)
		modulo = get_object_or_404(Anuncio, pk=id)
		if form.is_valid():
			curso = modulo.curso
			conteudo = form.save(commit=False)
			conteudo.usuario = request.user
			conteudo.save()
			messages.success(request, 'Anúncio cadastrado com sucesso!')
			proxima = request.GET.get("proxima")
	else:
		form = ConteudoForm()
		modulo = get_object_or_404(Modulo, pk=id)
	context = {
		'form': form,
		'modulo': modulo,
	}
	return render(request, 'cadastro_conteudo.html', context)

@login_required
def editar_curso(request, id):
	curso = get_object_or_404(Curso, pk=id)
	form = CursoForm(instance=curso)

	if(request.method == 'POST'):
		form = CursoForm(request.POST, request.FILES, instance=curso)

		if(form.is_valid()):
			form.save()
			messages.success(request, 'Curso editado com sucesso!')
			proxima = request.GET.get("proxima")
			if not proxima:
				proxima = "cursos"
			return redirect(proxima)
		else:
			return render(request, 'editar_curso.html', {'form': form, 'curso': curso})
	else:
		return render(request, 'editar_curso.html', {'form': form, 'curso': curso})

@login_required
def editar_modulo(request, id):
	modulo = get_object_or_404(Modulo, pk=id)
	form = ModuloForm(instance=modulo)

	if(request.method == 'POST'):
		form = ModuloForm(request.POST, request.FILES, instance=modulo)
		curso = modulo.curso
		if(form.is_valid()):
			form.save()
			messages.success(request, 'Módulo editado com sucesso!')
			return redirect('area_restrita_modulos', curso.id)
		else:
			return render(request, 'editar_modulo.html', {'form': form, 'modulo': modulo})
	else:
		return render(request, 'editar_modulo.html', {'form': form, 'modulo': modulo})

@login_required
def editar_conteudo(request, id):
	conteudo = get_object_or_404(Conteudo, pk=id)
	form = ConteudoForm(instance=conteudo)
	if(request.method == 'POST'):
		form = ConteudoForm(request.POST, request.FILES, instance=conteudo)
		modulo = conteudo.modulo
		if(form.is_valid()):
			form.save()
			messages.success(request, 'Conteúdo editado com sucesso!')
			return redirect('area_restrita_conteudos', modulo.id)
		else:
			return render(request, 'editar_conteudo.html', {'form': form, 'conteudo': conteudo})
	else:
		return render(request, 'editar_conteudo.html', {'form': form, 'conteudo': conteudo})

@login_required
def deletar_curso(request, pk):
    dado = Curso.objects.get(id=pk)
    if request.method == 'POST':
    	dado.delete()
    	messages.error(request, 'Curso deletado com sucesso!')
    	proxima = request.GET.get("proxima")
    	if not proxima:
    		proxima = "cursos"
    	return redirect(proxima)
    return render(request, 'deletar_curso.html', {'dado': dado})

@login_required
def deletar_modulo(request, pk):
    dado = Modulo.objects.get(id=pk)
    curso = dado.curso
    if request.method == 'POST':
    	dado.delete()
    	messages.error(request, 'Módulo deletado com sucesso!')
    	return redirect('area_restrita_modulos', curso.id)
    return render(request, 'deletar_modulo.html', {'dado': dado, 'curso': curso})

@login_required
def deletar_conteudo(request, pk):
    dado = Conteudo.objects.get(id=pk)
    conteudo = dado.modulo
    if request.method == 'POST':
    	dado.delete()
    	messages.error(request, 'Conteúdo deletado com sucesso!')
    	return redirect('area_restrita_conteudos', conteudo.id)
    return render(request, 'deletar_conteudo.html', {'dado': dado, 'conteudo': conteudo})

