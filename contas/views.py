from django.shortcuts import render
from .models import Pessoa, Conta

def mostrar_formulario_cadastro(request):
  contexto = {'msg':""}
  if request.method == 'POST':
    pessoa = Pessoa()
    pessoa.nome = request.POST.get('nome')
    pessoa.cpf = request.POST.get('cpf')
    pessoa.email = request.POST.get('email')
    pessoa.telefone = request.POST.get('telefone')
    pessoa.genero = request.POST.get('genero')
    pessoa.save()
    return render(request, 'login.html')

  return render(request, 'index.html', contexto)

def mostrar_pessoas(request):
  pessoas = Pessoa.objects.all()

  return render(request, 'pessoas.html', {'dados': pessoas})

def login(request):
  if request.method == 'POST':
    email_formulario = request.POST.get('login')
    pessoa_bd = Pessoa.objects.filter(email=email_formulario).first()
    if pessoa_bd is not None:
      argumento = {
        'pessoa': pessoa_bd
      }
      return render(request, 'conta.html', argumento)
    return render(request, 'login.html', {'msg' : 'O email informado não está cadastrado na base.'})
  
  return render(request, 'login.html')
    
def cadastrar_conta(request):
  if request.method == 'POST':
    pessoa_bd = Pessoa.objects.filter(email=request.POST.get('pessoa')).first()
    if pessoa_bd is not None:
      conta = Conta()
      conta.pessoa = pessoa_bd
      conta.numero_conta = request.POST.get('numero_conta')
      conta.saldo = request.POST.get('saldo')
      conta.agencia = request.POST.get('agencia')
      conta.save()
      argumento = {
        'pessoa': pessoa_bd,
        'conta': Conta.objects.filter(pessoa=pessoa_bd).first()
      }
      return render(request, 'pessoa_filtrada.html', argumento)
    else:
      return render(request, 'index.html', {'msg': 'Cadastre-se para criar a conta!'})
  return render(request, 'conta.html')

  