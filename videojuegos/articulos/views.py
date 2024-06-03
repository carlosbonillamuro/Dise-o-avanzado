from django.shortcuts import render,redirect
from articulos.models import Articulos, Categoria
from articulos.forms import FormArticulo

def lista_articulos(request):
    articulos = Articulos.objects.all()

    return render(request,'articulos.html',{'articulos':articulos})

def eliminar_articulos(request,id):
    Articulos.objects.get(id=id).delete()
    return redirect('lista_articulos')

def nuevo_articulo(request):
    if request.method == 'POST':
        form = FormArticulo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_articulos')
    else:
        form=FormArticulo()
    return render(request,'nuevo_articulo.html',{'form':form})

def editar_articulos(request,id):
    articulo = Articulos.objects.get(id=id)
    if request.method == 'POST':
        form = FormArticulo(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('lista_articulos')
    else:
        form=FormArticulo(instance=articulo)
    return render(request,'editar_articulo.html',{'form':form})
