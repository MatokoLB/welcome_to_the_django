from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator
from .models import Cliente, Endereco,Relato
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import View
from .utils import render_to_pdf 





# Create your views here.
#pagina clinetes
@has_permission_decorator('cadastrar_cliente')
def cliente(request):
    if request.method == "GET":
        return render(request, 'cadastra_cliente.html',)
    if request.method == "POST":
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        rg = request.POST.get('rg')
        data_nascimento = request.POST.get('data_nascimento')
        sexo = request.POST.get('sexo')
        cliente =  Cliente.objects.filter(cpf=cpf)

        if cliente.exists():
            #utilizar mensagen do django
            messages.add_message(request, messages.INFO, 'clinete ja existe')
            return redirect(reverse('cliente'))
        cliente = Cliente.objects.create(nome=nome,cpf=cpf,rg=rg,data_nascimento=data_nascimento,sexo=sexo)
        messages.add_message(request, messages.SUCCESS, 'cliente cadastrado com sucesso')
        return redirect(reverse('cliente'))

#pagina lista de clientes
@has_permission_decorator('cadastrar_cliente')
def lista_cliente(request): 

    if request.method == "GET":
        #filtar por nome
        nome = request.GET.get('nome')
        limpar = request.GET.get('limpar')

        clientes = Cliente.objects.all()

    if nome or limpar:
        if nome:
            clientes = Cliente.objects.filter(nome__icontains=nome)
        if limpar:
            clientes = Cliente.objects.all()

    return render(request, 'lista_cliente.html', {'clientes': clientes })


##gerador de pdf
# class GereratePdf(View):
#     def get(self, request, *args, **kwargs):
#         pdf = render_to_pdf('pdf.html')
#         return HttpResponse(pdf, content_type='application/pdf')

class GereratePdf(View):
    def get(self,request, id , *args, **kwargs):
        cliente =  Cliente.objects.get(id=id)
        endereco = Endereco.objects.filter(ecliente=id).first()
        data = {
      
        }
        pdf = render_to_pdf('pdf.html',{"cliente": cliente ,"endereco": endereco })
        if pdf:
            response=HttpResponse(pdf,content_type='application/pdf')
            filename = "Report_for_%s.pdf"
            content = "inline; filename= %s" %(filename)
            response['Content-Disposition']=content
            return response
        return HttpResponse("Page Not Found")


#pagina deleta cliente
@has_permission_decorator('cadastrar_cliente')
def deletar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    messages.add_message(request, messages.SUCCESS, 'cliente excluido')
    return redirect(reverse('lista_cliente'))


#paginas de editar e atualizar cliente
@has_permission_decorator('cadastrar_cliente')
def editar_cliente(request, id):
    cliente =  Cliente.objects.get(id=id)
    
    ## pega relatos de um unico cliente / endereço
    relatos = Relato.objects.filter(cliente=id)
    enderecos = Endereco.objects.filter(ecliente=id)
    return render(request, "update_cliente.html", 
    {"cliente": cliente , "relatos": relatos , "enderecos" : enderecos })


@has_permission_decorator('cadastrar_cliente')
def update_cliente(request, id):
    if request.method == "POST":
       
        new_nome = request.POST.get('nome')
        new_cpf = request.POST.get('cpf')
        new_rg = request.POST.get('rg')
        new_data_nascimento = request.POST.get('data_nascimento')
        new_sexo = request.POST.get('sexo')


        updated_cliente = Cliente.objects.get(id=id)
        updated_cliente.nome = new_nome
        updated_cliente.cpf = new_cpf
        updated_cliente.rg = new_rg
        updated_cliente.data_nascimento = new_data_nascimento
        updated_cliente.sexo = new_sexo

        updated_cliente.save()
        messages.add_message(request, messages.SUCCESS, "cliente atualizado")
        return redirect(reverse('lista_cliente'))



##relatos dos clietes 
@has_permission_decorator('cadastrar_cliente')
def relato(request):
    if request.method == "GET":
        clientes = Cliente.objects.all()
        return render(request, 'add_relato.html', {"clientes": clientes})
    if request.method == "POST":
        cliente = request.POST.get('cliente')
        pedido = request.POST.get('pedido')
        detalhes_pedido = request.POST.get('detalhes_pedido')
        relato = Relato.objects.create(cliente_id=cliente,pedido=pedido,detalhes_pedido=detalhes_pedido)
        relato.save()
        messages.add_message(request, messages.SUCCESS, "pedido salvo")
        return redirect(reverse('relato'))
        
        
@has_permission_decorator('cadastrar_cliente')
def editar_relato(request, id ):
    if request.method == "GET":
        relato = Relato.objects.get(id=id)
        clientes = Cliente.objects.filter(id=id)
    ## pega relatos de um unico cliente
        return render(request, "editar_relato.html", {"clientes": clientes , "relato": relato})
  
    if request.method == "POST":
        pedido = request.POST.get('pedido')
        detalhes_pedido = request.POST.get('detalhes_pedido')

      
        relato = Relato.objects.get(id=id)
        relato.pedido=pedido
        relato.detalhes_pedido=detalhes_pedido
        relato.save()

        messages.add_message(request, messages.SUCCESS, "atualizado salvo")
        return redirect(reverse('relato'))

@has_permission_decorator('cadastrar_cliente')
def deletar_relato(request, id ):
    relato = Relato.objects.get(id=id)
    relato.delete()
    messages.add_message(request, messages.SUCCESS, 'relato excluido')
    return redirect(reverse('lista_cliente'))


##endereço dos clietes 

@has_permission_decorator('cadastrar_cliente')
def endereco(request):
    if request.method == "GET":
        clientes = Cliente.objects.all()
        return render(request, 'endereco.html', {"clientes": clientes })
    if request.method == "POST":
        ecliente = request.POST.get('ecliente')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        bairro = request.POST.get('bairro')
        cep = request.POST.get('cep')
        
    endereco = Endereco.objects.create( ecliente_id = ecliente ,rua=rua,numero=numero,complemento=complemento,bairro=bairro,cep=cep)
    endereco.save()

    messages.add_message(request, messages.SUCCESS, " endereco salvo")
    return redirect(reverse('endereco'))


@has_permission_decorator('cadastrar_cliente')
def editar_endereco(request, id ):
    if request.method == "GET":
        endereco = Endereco.objects.get(id=id)
        clientes = Cliente.objects.filter(id=id)
    ## pega relatos de um unico cliente
        return render(request, "editar_endereco.html", {"clientes": clientes , "endereco": endereco})
  
    if request.method == "POST":

      
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        bairro = request.POST.get('bairro')
        cep = request.POST.get('cep')
      


        endereco = Endereco.objects.get(id=id)
        endereco.rua=rua
        endereco.numero=numero
        endereco.complemento=complemento
        endereco.bairro=bairro
        endereco.cep=cep
        endereco.save()

        messages.add_message(request, messages.SUCCESS, "endereço atualizado")
        return redirect(reverse('endereco'))

    
@has_permission_decorator('cadastrar_cliente')
def deletar_endereco(request, id ):
    endereco = Endereco.objects.get(id=id)
    endereco.delete()
    messages.add_message(request, messages.SUCCESS, 'endereço excluido')
    return redirect(reverse('lista_cliente'))
