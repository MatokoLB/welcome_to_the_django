import imp
from rolepermissions.roles import AbstractUserRole


##criando as permisoes dos usuarios
class Administrativo(AbstractUserRole):
    available_permissions = {
        'cadastrar_cliente': True,
        'imprimir_relatorio': True,
        'cadastrar_funcionario': True,
    }


class Recpecao(AbstractUserRole):
      available_permissions = {
        'cadastrar_cliente': True,
      }