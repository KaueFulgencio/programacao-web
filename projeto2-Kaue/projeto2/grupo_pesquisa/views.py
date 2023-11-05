from django.shortcuts import render, redirect

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

def adicionar_foto_integrante(request, integrante_id):
    integrante = Integrante.objects.get(pk=integrante_id)

    if request.method == 'POST':
        integrante.foto = request.FILES['foto']
        integrante.save()

        return redirect('detalhes_integrante', integrante_id=integrante.id)

    return render(request, 'adicionar_foto_integrante.html', {'integrante': integrante})