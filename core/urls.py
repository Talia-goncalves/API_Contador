from django.urls import path
from contador.views import mostrar_dados, receber_dados 

urlpatterns = [
    path('', mostrar_dados, name='mostrarDados'),
    path('api/', receber_dados, name='receberDados')

]