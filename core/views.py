from asyncio.proactor_events import _ProactorDuplexPipeTransport
from json import load
from multiprocessing import context
from re import template
from django import http
from django.shortcuts import render
from core.models import Produto
from .models import Produto
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação com Django framework',
        'django':  'django é muito legal',
        'produtos': produtos
    }
    return render(request,'index.html', context)

def contato(request):
    return render(request, 'contato.html')
    
def produtos(request, pk):
    #prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request, ):
    template = loader.get_template('500.hmtl')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf9', status=500)