from django import forms
from .models import Integrante, Publicacao, GrupoPesquisa

class PublicacaoForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ['titulo', 'ano_publicacao', 'onde_publicado', 'autores']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # campos opcionais não são obrigatorios se escolher publicacao existente
        self.fields['titulo'].required = False
        self.fields['ano_publicacao'].required = False
        self.fields['onde_publicado'].required = False
        self.fields['autores'].required = False

    def clean(self):
        cleaned_data = super().clean()
        if not any(cleaned_data.values()):  # Verifica se algum campo foi preenchido
            raise forms.ValidationError("Preencha ao menos um campo para a publicação existente.")
        return cleaned_data

        
class IntegranteForm(forms.ModelForm):
    class Meta:
        model = Integrante
        fields = ['nome', 'tipo', 'foto']

class GrupoPesquisaForm(forms.ModelForm):
    class Meta:
        model = GrupoPesquisa
        fields = ['nome', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  
        }

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) < 3:
            raise forms.ValidationError("O nome do grupo deve ter mais de 3 caracteres.")
        return nome
        
        