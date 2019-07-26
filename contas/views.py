from django.shortcuts import render
from .models import Pessoa

def mostrar_formulario_cadastro(request):
  contexto = {'msg':""}
  if request.method == 'POST':
    pessoa = Pessoa()
    pessoa.nome = request.POST.get('nome')
    pessoa.cpf = request.POST.get('cpf')
    pessoa.cpf = request.POST.get('email')
    pessoa.cpf = request.POST.get('telefone')
    pessoa.cpf = request.POST.get('genero')
    pessoa.save()
    contexto = {'msg': 'Aeeee Parabéns :)'}
  return render(request, 'index.html', contexto)

def mostrar_pessoas(request):
  pessoas = Pessoa.objects.all()

  return render(request, 'pessoas.html', {'dados': pessoas})