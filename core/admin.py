
from django.contrib import admin

# Register your models here.
from .models import Produto, Cliente, Aluno

class ProdutoADmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class CLienteAdmin(admin.ModelAdmin):
    list_display = ('nome','sobrenome', 'email')
    


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'turma', 'adjetivo', 'foto')

admin.site.register(Produto, ProdutoADmin)
admin.site.register(Cliente, CLienteAdmin)
admin.site.register(Aluno,AlunoAdmin)