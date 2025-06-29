from django.urls import path
from . import views



urlpatterns = [
    # ... outras rotas
    path('comentar/<int:post_id>/', views.comentar_post, name='comentar_post'),
    path('curtir/<int:post_id>/', views.curtir_post, name='curtir_post'),
    path('postar/', views.nova_postagem, name='postar'),


]