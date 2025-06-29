from django.contrib import admin
from django.urls import path, include
from socialapp.views import (
    index, sobre, postar, contato,
    new_avalia, editar_avalia, deleta_avalia,
    nova_postagem, deleta_post, editar_post
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Página inicial = feed com posts públicos
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato'),

    # Avaliações
    path('new_avalia/', new_avalia, name='new_avalia'),
    path('editar_avalia/<str:id>', editar_avalia, name='editar_avalia'),
    path('deleta_avalia/<int:id>', deleta_avalia, name='deleta_avalia'),

    # Postagens
    path('postar/', nova_postagem, name='postar'),
    path('editar_post/<str:id>', editar_post, name='editar_post'),
    path('deleta_post/<int:id>', deleta_post, name='deleta_post'),

    # Usuário (cadastro/login)
    path('usuario/', include('usuario.urls')), 
    path('', include('socialapp.urls')),
    ]