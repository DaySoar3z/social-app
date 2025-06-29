from django.urls import path
from django.contrib.auth.views import  LogoutView
from .views import login_personalizado
from django.urls import reverse_lazy
from .views import new_usuario, conecte_se, cadastro

urlpatterns = [
    path('login/', login_personalizado, name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),
    path('new_usuario/', new_usuario, name='new_usuario'),
    path('conecte_se/', conecte_se, name='conecte_se'),
    path('cadastro/', cadastro, name='cadastro'),
]