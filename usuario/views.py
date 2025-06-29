from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UsuarioForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm




# Create your views here.
def new_usuario(request):
    form =UsuarioForm(request.POST)
    if request.method =='POST':
        form =UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            return redirect('login')
        return render(request,'usuario/usuario.html',{'form':form})
    
def login_personalizado(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(request, username=username, password=senha)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return redirect('conecte_se')
    else:
        return redirect('conecte_se')
    
def conecte_se(request):
    return render(request, 'usuario/conecte_se.html')


def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha1 = request.POST.get('password1')
        senha2 = request.POST.get('password2')

        if senha1 != senha2:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('conecte_se')

        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Esse nome de usuário já está em uso.')
            return redirect('conecte_se')

        novo_usuario = User.objects.create_user(username=username, email=email, password=senha1)
        login(request, novo_usuario)  # faz login automático
        return redirect('index')  # leva direto para os posts

    return redirect('conecte_se')
