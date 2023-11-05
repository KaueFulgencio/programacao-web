from django import forms
from .models import Integrante, Publicacao

class IntegranteForm(forms.ModelForm):
    class Meta:
        model = Integrante
        fields = ['nome', 'tipo', 'foto']

class PublicacaoForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ['integrante', 'titulo', 'ano_publicacao', 'onde_publicado', 'autores']
