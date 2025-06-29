from django.shortcuts import render, redirect, get_object_or_404
from socialapp.forms import AvaliaForms, PostagemForms
from socialapp.models import Avalia, Postagem
from .models import Comentario, Curtida
from .forms import ComentarioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    postagens = Postagem.objects.all().order_by('-data_postagem')
    return render(request, 'social/index.html', {'postagens': postagens})

def contato(request):
    return render(request, 'social/contact.html')

def sobre(request):
    return render(request, 'social/about.html')

def postar(request):
    return nova_postagem(request) 

def new_avalia(request):
    avas = Avalia.objects.all()
    form = AvaliaForms()
    if request.method == 'POST':
        form = AvaliaForms(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            form = AvaliaForms()
    return render(request, 'social/new_avalia.html', {'form': form, 'avas': avas})

def editar_avalia(request, id):
    avaliado = get_object_or_404(Avalia, pk=id)
    form = AvaliaForms(instance=avaliado)
    avas = Avalia.objects.all()
    if request.method == "POST":
        form = AvaliaForms(request.POST, request.FILES, instance=avaliado)
        if form.is_valid():
            form.save()
            return redirect('new_avalia')
    return render(request, 'social/editar_avalia.html', {'form': form, 'avas': avas, 'avaliado': avaliado})

def deleta_avalia(request, id):
    avaliado = get_object_or_404(Avalia, pk=id)
    form = AvaliaForms(instance=avaliado)
    avas = Avalia.objects.all()
    if request.method == "POST":
        avaliado.delete()
        return redirect('new_avalia')
    return render(request, 'social/deleta_avalia.html', {'avaliado': avaliado, 'form': form, 'avas': avas})

@login_required
def editar_post(request, id):
    post = get_object_or_404(Postagem, pk=id)

    if request.user != post.autor_postagem:
        messages.error(request, "Você não tem permissão para editar este post.")
        return redirect('index')

    if request.method == "POST":
        form = PostagemForms(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostagemForms(instance=post)

    posts = Postagem.objects.filter(autor_postagem=request.user).order_by('-data_postagem')
    return render(request, 'social/editar_post.html', {
        'form': form,
        'post': post,
        'posts': posts
    })


@login_required
def deleta_post(request, id):
    post = get_object_or_404(Postagem, pk=id)
    if request.user != post.autor_postagem:
        messages.error(request, "Você não tem permissão para excluir este post.")
        return redirect('index')

    if request.method == "POST":
        post.delete()
        return redirect('index')

    return render(request, 'social/deleta_post.html', {'post': post})

@login_required
def comentar_post(request, post_id):
    post = get_object_or_404(Postagem, pk=post_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.post = post  
            comentario.save()
    return redirect('index')

@login_required
def curtir_post(request, post_id):
    post = get_object_or_404(Postagem, pk=post_id)

    curtida, created = Curtida.objects.get_or_create(
        post=post,  # aqui vai o objeto Postagem
        usuario=request.user
    )

    if not created:
        curtida.delete()

    return redirect('index')

@login_required
def nova_postagem(request):
    if request.method == 'POST':
        form = PostagemForms(request.POST, request.FILES)
        if form.is_valid():
            nova = form.save(commit=False)
            nova.autor_postagem = request.user
            nova.save()
            return redirect('index')
    else:
        form = PostagemForms()
    posts = Postagem.objects.filter(autor_postagem=request.user)
    return render(request, 'social/new_post.html', {'form': form, 'posts': posts})