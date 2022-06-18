

from gc import get_objects
from http.client import OK
from re import template
from django import http
from django.shortcuts import render
from core.models import Produto, Aluno
from .models import Produto, Aluno
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from core.templates import turmas
# Create your views here.

def index(request):
    alun = Aluno.objects.all()
    
    context = {
    'alunos': alun,
    
    }
    return render(request,'index.html', context)

def contato(request):
    return render(request, 'contato.html')
    
def produtos(request, pk):
    #prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=id)
    
    context = {
        'produto': prod,
        
        
    }
    return render(request, 'produto.html', context)

def aluno(request, pk):
    alun = get_object_or_404(Aluno,pk=pk)
    lista = Aluno.objects.all()
    context = {
    'aluno': alun,
    'lista': lista
    }
    return render(request, 'aluno.html', context)

def turma(request):    

    return render(request, 'turmas/turmas.html')


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request, ):
    template = loader.get_template('500.hmtl')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf9', status=500)

