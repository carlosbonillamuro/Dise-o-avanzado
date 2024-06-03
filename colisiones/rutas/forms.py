from dataclasses import fields
from django import forms 
from rutas.models import rutas,Trenes,Personal

class FormRuta(forms.ModelForm):
    
    class Meta:
        model = rutas
        fields = '__all__'
        # exclude = 'stock'

        widgets = {
            'viajes': forms.NumberInput(attrs={'class':'form-control'}),
            'maquina': forms.Select(attrs={'class':'form-control'}),
            'maquinista': forms.Select(attrs={'class':'form-control'}),
            'origen': forms.Select(attrs={'class':'form-control'}),
            'destino': forms.Select(attrs={'class':'form-control'}),
            'salida': forms.DateInput(attrs={'type': 'date'}),
            'llegada': forms.DateInput(attrs={'type': 'date'}),
        }

class FormTrenes(forms.ModelForm):
    
    class Meta:
        model = Trenes
        fields = '__all__'
        # exclude = 'stock'

        widgets = {
            'idmaquina': forms.TextInput(attrs={'class':'form-control'}),
            'idgps': forms.TextInput(attrs={'class':'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class':'form-control'}),
            'marca': forms.TextInput(attrs={'class':'form-control'}),
            'modelo': forms.TextInput(attrs={'class':'form-control'}),
            'serie': forms.DateInput(attrs={'class':'form-control'}),
                   
                    }

class FormPersonal(forms.ModelForm):
    
    class Meta:
        model = Personal
        fields = '__all__'
        # exclude = 'stock'

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'cargo': forms.Select(attrs={'class':'form-control'}),
            'empleado': forms.TextInput(attrs={'class':'form-control'}),
            'licencia': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.TextInput(attrs={'class':'form-control'}),
            'ingreso':  forms.DateInput(attrs={'type': 'date'}),
            'segurosocial': forms.TextInput(attrs={'class':'form-control'}),

        }
