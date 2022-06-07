from itertools import product
from django.contrib import admin

# Register your models here.
from .models import Produto, Cliente

class ProdutoADmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class CLienteAdmin(admin.ModelAdmin):
    list_display = ('nome','sobrenome', 'email')
    
admin.site.register(Produto, ProdutoADmin)
admin.site.register(Cliente, CLienteAdmin)
