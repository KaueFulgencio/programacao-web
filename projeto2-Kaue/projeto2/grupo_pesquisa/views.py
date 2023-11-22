from django.shortcuts import render, redirect

from django.shortcuts import get_object_or_404

#modelos
from .models import Integrante, Publicacao, GrupoPesquisa
from .forms import IntegranteForm, PublicacaoForm

def lista_integrantes(request):
    integrantes = Integrante.objects.order_by('nome')
    integrantes_unicos = []
    integrante_atual = None

    for integrante in integrantes:
        if integrante.nome != integrante_atual:
            integrante_atual = integrante.nome
            integrantes_unicos.append(integrante)

    return render(request, 'lista_integrantes.html', {'integrantes': integrantes_unicos})

def detalhes_integrante(request, integrante_id):
    integrante = get_object_or_404(Integrante, pk=integrante_id)
    publicacoes = integrante.publicacoes.all()
    publicacoes_disponiveis = Publicacao.objects.all()
    
    if request.method == 'POST':
        form = PublicacaoForm(request.POST)
        if form.is_valid():
            publicacao_id = request.POST.get('publicacao_id')  # Obtém o ID da publicação selecionada
            if publicacao_id:
                publicacao_existente = get_object_or_404(Publicacao, pk=publicacao_id)
                integrante.publicacoes.add(publicacao_existente)
                return redirect('detalhes_integrante', integrante_id=integrante_id)

    form = PublicacaoForm()
    
    return render(request, 'detalhes_integrante.html', {
        'integrante': integrante,
        'publicacoes': publicacoes,
        'publicacoes_disponiveis': publicacoes_disponiveis,
        'form': form,
    })

def adicionar_foto_integrante(request, integrante_id):
    integrante = Integrante.objects.get(pk=integrante_id)

    if request.method == 'POST':
        integrante.foto = request.FILES['foto']
        integrante.save()

        return redirect('detalhes_integrante', integrante_id=integrante.id)

    return render(request, 'adicionar_foto_integrante.html', {'integrante': integrante})

def descricao_grupo(request):
    grupos_pesquisa = GrupoPesquisa.objects.order_by('nome')
    grupos_unicos = []
    grupo_atual = None

    for grupo in grupos_pesquisa:
        if grupo.nome != grupo_atual:
            grupo_atual = grupo.nome
            grupos_unicos.append(grupo)

    return render(request, 'descricao_grupo.html', {'grupos_pesquisa': grupos_unicos})

def adicionar_integrante(request):
    if request.method == 'POST':
        form = IntegranteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_integrantes')
    else:
        form = IntegranteForm()
    
    return render(request, 'adicionar_integrante.html', {'form': form})


