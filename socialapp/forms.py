from django import forms
from socialapp.models import Avalia, Postagem,Perfil, Telefone,Perfil_post, Comentario

class AvaliaForms(forms.ModelForm):
    class Meta:
        model = Avalia
        fields ="__all__"


class PostagemForms(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = ['titulo_postagem', 'conteudo_postagem', 'id_avalia']

class PerfilForms(forms.ModelForm):
    class Meta:
        model = Perfil
        fields ="__all__"


class TelefoneForms(forms.ModelForm):
    class Meta:
        model = Telefone
        fields ="__all__"


class PerfilPostForms(forms.ModelForm):
    class Meta:
        model = Perfil_post
        fields ="__all__"
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.TextInput(attrs={'placeholder': 'Digite seu comentário...'})
        }


