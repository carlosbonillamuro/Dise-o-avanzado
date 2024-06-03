from django.shortcuts import render

def mensaje(request):
    return render(request,'mensaje.html')

def funcion_nombre(request):
    nombre='Carlos'
    return render(request,'nombre.html',{'nombre':nombre})
# Create your views here.
