from django.shortcuts import render

def funcion_hola(request):
    return render(request,'hola.html')

def funcion_calculadora(request):
    return render(request,'calculadora.html')

# Create your views here.
