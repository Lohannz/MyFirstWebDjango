from unicodedata import name
from django.urls import URLPattern, path
from .views import index, contato, produtos


urlpatterns = [
    path('', index , name='index'),
    path('contato', contato),
    path('produtos/<int:pk>', produtos, name="produto"),
]