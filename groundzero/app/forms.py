from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import widgets
from .models import Contacto, Producto ,widgets
from .validators import MaxSizeFileValidator
from django.forms import ValidationError



class ContactoForm(forms.ModelForm):
   
    class Meta:
            model = Contacto
            fields = '__all__'

class ProductoForm(forms.ModelForm):

    #nombre = forms.CharField(min_length=3, max_length=40)
    #imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=4)] )
    #direccion = forms.CharField(min_length=3)

    class Meta:
        model = Producto
        fields = ["rut_id","nombre","direccion","comuna","pais","telefono","moneda_pago","email","Tipo_Proveedor", "imagen"]
        #fields = '__all__'


    #def clean_rut_id(self):
    #    rut_id = self.cleaned_data["rut_id"]
    #    existe = Producto.objects.filter(rut_id=rut_id).exists()
    #    if existe:
    #        raise ValidationError("Este Rut ya existe")
    #    return rut_id