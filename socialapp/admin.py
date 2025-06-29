from django.contrib import admin
from socialapp.models import Avalia, Postagem, Perfil,Telefone,Perfil_post

# Register your models here.
admin.site.register(Avalia)
admin.site.register(Postagem)
admin.site.register(Perfil)
admin.site.register(Telefone)
admin.site.register(Perfil_post)