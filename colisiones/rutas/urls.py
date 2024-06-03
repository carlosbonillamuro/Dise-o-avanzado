from django.urls import path
from rutas import views, views_rutas

urlpatterns = [

    #path('rutas/', views.rutas_list, name='lista_articulos'),
    #path('rutas/nuevo', views.nuevo_articulo, name='nuevo_articulo'),
    #path('rutas/eliminar/<int:id>', views.eliminar_articulos, name='eliminar_articulos'),
    #path('rutas/editar/<int:id>',views.editar_articulos,name='editar_articulos'),

    path('', views_rutas.BienvenidaView.as_view(), name='bienvenida'),
    
    path('rutas', views_rutas.ListaRutas.as_view(),name='rutas_list'),
    path('rutas/nuevo', views_rutas.NuevaRutaView.as_view(),name='nueva_rutas'),
    path('rutas/editar/<int:pk>', views_rutas.EditarRutaView.as_view(),name='editar_rutas'),
    path('rutas/eliminar/<int:pk>', views_rutas.EliminarRutasView.as_view(),name='eliminar_rutas'),    
    
    path('trenes', views_rutas.ListaTrenes.as_view(),name='trenes_list'),
    path('trenes/nuevo', views_rutas.NuevaTrenesView.as_view(),name='nueva_trenes'),
    path('trenes/editar/<int:pk>', views_rutas.EditarTrenesView.as_view(),name='editar_trenes'),
    path('trenes/eliminar/<int:pk>', views_rutas.EliminarTrenesView.as_view(),name='eliminar_trenes'),    
    
    path('personal', views_rutas.ListaPersonal.as_view(),name='personal_list'),
    path('personal/nuevo', views_rutas.NuevaPersonalView.as_view(),name='nueva_personal'),
    path('personal/editar/<int:pk>', views_rutas.EditarPersonalView.as_view(),name='editar_personal'),
    path('personal/eliminar/<int:pk>', views_rutas.EliminarPersonalView.as_view(),name='eliminar_personal'),    

]
