from django.shortcuts import render
from django.db.utils import IntegrityError
from django.http import JsonResponse
from .serializers import UsuarioSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            novo_usuario = Usuario()
            novo_usuario.email = email.POST.get('email')
            novo_usuario.nome = request.POST.get('nome')
            novo_usuario.senha = request.POST.get('senha')
            
            try:
                novo_usuario.save()
            except IntegrityError:
                pass

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios/usuarios.html', usuarios)

@api_view(['GET', 'POST'])
def cria_usuarios(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        nome = data.get('nome')
        senha = data.get('senha')
        
        if email and nome and senha:
            try:
                novo_usuario = Usuario(email=email, nome=nome, senha=senha)
                novo_usuario.save()
                return Response({'message': 'Usuário criado com sucesso!'}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({'error': 'Email já está em uso.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Todos os campos são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)

    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)




