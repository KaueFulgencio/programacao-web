from django.shortcuts import render

from django.shortcuts import get_object_or_404
from .models import Integrante, Publicacao

def descricao_grupo(request):
    return render(request, 'descricao_grupo.html')

def lista_integrantes(request):
    integrantes = Integrante.objects.all()
    return render(request, 'lista_integrantes.html', {'integrantes': integrantes})

def detalhes_integrante(request, integrante_id):
    integrante = get_object_or_404(Integrante, pk=integrante_id)
    publicacoes = Publicacao.objects.filter(integrante=integrante)
    return render(request, 'detalhes_integrante.html', {'integrante': integrante, 'publicacoes': publicacoes})
