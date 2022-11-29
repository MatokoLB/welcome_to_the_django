from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator
from .models import Users
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import View



def home(resquest):
    return render(resquest, 'home.html' )

# Create your views here.

##pagina de cadastro funcionarios com pemissoes do rolespemissions
# @has_permission_decorator('cadastrar_funcionario')
# retirei a permisaso para nao atrapalha o primeiro acesso(necessario a criaçao de um superUser)
def cadastrar_funcionario(request):
    if request.method == "GET":
        funcionarios = Users.objects.filter(cargo="R")
        return render(request, 'cadastrar_funcionario.html', {'funcionarios': funcionarios})
    if request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cargo = request.POST.get('cargo')
        user = Users.objects.filter(email=email)

        if user.exists():
            #utilizar mensagen do django
            
            messages.add_message(request, messages.WARNING, 'Email ja existente')
            return redirect(reverse('cadastrar_funcionario'))
            
        user = Users.objects.create_user(username=email, email=email , first_name=nome, last_name=sobrenome, password=senha, cargo="R")
        messages.add_message(request, messages.SUCCESS, 'funcionario criado com sucesso')
        return redirect(reverse('cadastrar_funcionario'))


##pagina de login
def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            # return HttpResponse("ja esta logado")
            messages.add_message(request, messages.INFO, 'funcionario ja esta logado')
            return redirect(reverse('lista_cliente'))
        return render(request, 'login.html')
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=login, password=senha)

        if not user:
            #Redirecionar com mensagem de erro
            messages.add_message(request, messages.INFO, 'funcionario inexistente')
            return redirect(reverse('login'))

        auth.login(request, user)
        #return HttpResponse('Usuario logado com sucesso')
        messages.add_message(request, messages.INFO, 'funcionario logado com sucesso, seja bem -vindo')
        return redirect(reverse('lista_cliente'))


##pagina de logout
def logout(request):
    ## limpa sesao
    request.session.flush()
    return redirect(reverse('login'))

#pagina de crud funcionario delte
@has_permission_decorator('cadastrar_funcionario')
def delete_funcionario(request, id):
    funcionario = get_object_or_404(Users, id=id)
    funcionario.delete()
    messages.add_message(request, messages.SUCCESS, 'funcionario excluido')
    return redirect(reverse('cadastrar_funcionario'))

#pagina de crud funcionario editar
@has_permission_decorator('cadastrar_funcionario')
def editar_funcionario(request, id):
    funcionario =  Users.objects.get(id=id)
    return render(request, "update_funcionario.html", {"funcionario": funcionario})

#pagina de crud funcionario update
@has_permission_decorator('cadastrar_funcionario')
def update_funcionario(request, id):
    if request.method == "POST":
        new_nome = request.POST.get('nome')
        new_sobrenome = request.POST.get('sobrenome')
        new_email = request.POST.get('email')

        # newsenha = request.POST.get('senha') nao funciona? pq as senhas nao sao quardadas 
        # em string, sao convertidadas em algoritimo de hash
        updated_user = Users.objects.get(id=id)
        updated_user.email = new_email
        updated_user.username = new_email
        updated_user.first_name = new_nome
        updated_user.last_name = new_sobrenome
        # updated_user.password = newsenha
        updated_user.save()
        messages.add_message(request, messages.SUCCESS, 'funcionario foi atualizado')
        return redirect(reverse('cadastrar_funcionario'))
        #return HttpResponse("funcionario atualizado")
