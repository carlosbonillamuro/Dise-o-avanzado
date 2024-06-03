from articulos.models import  Categoria, Articulos
from articulos.forms import FormCategoria
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
#from django.contrib.messages.view import SuccessMessageMixin,Fail 

class ListaCategorias(ListView):
    model = Categoria 

class NuevaCategoriasView(CreateView):
    model = Categoria
    #fields ='__all__'
    form_class = FormCategoria
    success_url = reverse_lazy('categoria_list')
    extra_context = {'accion':'Nueva'}
class EditarCategoriasView(UpdateView):
    model = Categoria
    #fields ='__all__'
    form_class = FormCategoria
    success_url = reverse_lazy('categoria_list')
    extra_context = {'accion':'Modificar'}
class EliminarCategoriasView(DeleteView):
    model = Categoria
    success_url = reverse_lazy('categoria_list')
    
    def form_valid(self, form):
        self.object =self.get_object()
        if Articulos.objects.filter(categoria=self.object):
            messages.error(self.request,'No se puede eliminar la categoría, Tiene articiculos agregados.')
            
        else: 
            self.object.delete()
            messages.success(self.request,'Se elimino con exito la categorias.')

        return HttpResponseRedirect(self.success_url)

#class SeleteView(SingleObjectTemplateResponseMixin, BaseDeleteView):

#    template_name_suffix ='_Confirm_Delete'    
        
class BienvenidaView(TemplateView):
    template_name = 'bienvenida.html'