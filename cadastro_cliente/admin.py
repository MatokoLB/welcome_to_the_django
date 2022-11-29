from django.contrib import admin
from .models import Cliente, Relato ,Endereco
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Relato)
admin.site.register(Endereco)