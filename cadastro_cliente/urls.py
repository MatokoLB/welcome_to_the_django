from django.urls import path
from . import views 
from .views import GereratePdf


urlpatterns = [
    path('cliente/', views.cliente , name="cliente"),
    path('lista_cliente/', views.lista_cliente , name="lista_cliente" ),
    path('deletar_cliente/<int:id>', views.deletar_cliente, name="deletar_cliente" ),
    path('editar_cliente/<int:id>', views.editar_cliente, name="editar_cliente" ),
    path('update_cliente/<int:id>', views.update_cliente, name="update_cliente" ),
    path('add_relato/', views.relato, name="relato" ),
    path('editar_relato/<int:id>', views.editar_relato, name="editar_relato" ),
    path('deletar_relato/<int:id>', views.deletar_relato, name="deletar_relato"),
    path('pdf/<int:id>', GereratePdf.as_view(), name="pdf" ),
]