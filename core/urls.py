import imp
from unicodedata import name
from xml.dom.minidom import Document
from django.urls import URLPattern, path
from .views import index, contato, produtos, aluno, turma

urlpatterns = [
    path('', index , name='index'),
    path('contato', contato),
    path('produtos/<int:pk>', produtos, name="produto"),
    path('aluno/<int:pk>', aluno, name="aluno"),
    path( 'turma/', turma, name="turma"),

]

