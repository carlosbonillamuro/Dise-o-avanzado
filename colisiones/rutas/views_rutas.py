from rutas.models import  rutas, Trenes, Personal
from rutas.forms import FormRuta, FormTrenes, FormPersonal 
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
#from django.contrib.messages.view import SuccessMessageMixin,Fail 

class ListaRutas(ListView):
    model = rutas 

class NuevaRutaView(CreateView):
    model = rutas
    #fields ='__all__'
    form_class = FormRuta
    success_url = reverse_lazy('rutas_list')
    extra_context = {'accion':'Nueva'}

class EditarRutaView(UpdateView):
    model = rutas
    #fields ='__all__'
    form_class = FormRuta
    success_url = reverse_lazy('rutas_list')
    extra_context = {'accion':'Modificar'}

class EliminarRutasView(DeleteView):
    model = rutas
    success_url = reverse_lazy('rutas_list')
    
    def form_valid(self,form):
        self.object =self.get_object()
        if Trenes.objects.filter(Trenes=self.object):
            messages.error(self.request,'No se puede eliminar, Tiene datos agregados.')
            
        else: 
            self.object.delete()
            messages.success(self.request,'Se elimino con exito.')

        return HttpResponseRedirect(self.success_url)

#class EliminarRutasView(DeleteView):
#    model = Trenes
#    success_url=reverse_lazy('rutas_list')
#    extra_context={'accion':'Eliminar'}


class ListaTrenes(ListView):
    model = Trenes 

class NuevaTrenesView(CreateView):
    model = Trenes
    #fields ='__all__'
    form_class = FormTrenes
    success_url = reverse_lazy('trenes_list')
    extra_context = {'accion':'Nuevo'}

class EditarTrenesView(UpdateView):
    model = Trenes
    #fields ='__all__'
    form_class = FormTrenes
    success_url = reverse_lazy('trenes_list')
    extra_context = {'accion':'Modificar'}

#class EliminarTrenesView(DeleteView):
#    model = Trenes
#    success_url = reverse_lazy('trenes_list')
    
#    def form_valid(self):
#        self.object =self.get_object()
#        if rutas.objects.filter(trenes=self.object):
#            messages.error(self.request,'No se puede eliminar el , Tiene datos agregados.')
#            
#        else: 
#            self.object.delete()
#            messages.success(self.request,'Se elimino con exito.')
#
#        return HttpResponseRedirect(self.success_url)

class EliminarTrenesView(DeleteView):
    model = Trenes
    success_url=reverse_lazy('trenes_list')
    extra_context={'accion':'Eliminar'}

class ListaPersonal(ListView):
    model = Personal 

class NuevaPersonalView(CreateView):
    model = Personal
    #fields ='__all__'
    form_class = FormPersonal
    success_url = reverse_lazy('personal_list')
    extra_context = {'accion':'Nuevo'}

class EditarPersonalView(UpdateView):
    model = Personal
    #fields ='__all__'
    form_class = FormPersonal
    success_url = reverse_lazy('personal_list')
    extra_context = {'accion':'Modificar'}

#class EliminarPersonalView(DeleteView):
#    model = Personal
#    success_url = reverse_lazy('personal_list')
    
#    def form_valid(self, form):
#        self.object =self.get_object()
#        if rutas.objects.filter(trenes=self.object):
#            messages.error(self.request,'No se puede eliminar la categoría, Tiene datos agregados.')
            
#        else: 
#            self.object.delete()
#            messages.success(self.request,'Se elimino con exito la categorias.')

#        return HttpResponseRedirect(self.success_url)

class EliminarPersonalView(DeleteView):
    model = Trenes
    success_url=reverse_lazy('personal_list')
    extra_context={'accion':'Eliminar'}


#class SeleteView(SingleObjectTemplateResponseMixin, BaseDeleteView):

#    template_name_suffix ='_Confirm_Delete'    
        
class BienvenidaView(TemplateView):
    template_name = 'bienvenida.html'