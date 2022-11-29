from atexit import register
from django import template
from cadastro_cliente.models import Relato,Cliente

register = template.Library()

##filtra infomaçoes 
@register.filter(name='get_relato')
def get_relato(id):
    relato = Relato.objects.filter(cliente=id)
    c = Cliente.objects.all().first()
    print(c.data_nascimento)     
    for i in relato:
        if relato:
            
            print(relato)
            return relato
        else:
            return False