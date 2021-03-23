from django.urls import path
from .views import index, contato, produtos, clientes, produto, cliente


urlpatterns = [
    path('', index, name='dashboard'),
    path('contato', contato, name='contato'),
    path('produtos', produtos, name='produtos'),
    path('clientes', clientes, name='clientes'),
    path('produto/<int:pk>', produto, name='produto'),
    path('cliente/<int:pk>', cliente, name='cliente')
]
