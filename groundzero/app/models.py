from django.db import models
from django.db.models.fields import CharField, TextField
from django.forms import widgets
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre

opciones_moneda = [
    [0, "$ CLP"],
    [1, "$ CUF"],
    [2, "US$ USD"],
    [3, "¥ Yen"],
    [4, "€ EUR"],
    [5, "£ GBP "],
    [6, "OTRO"]
] 

opciones_pais = [
    [0, "Chile"],
    [1, "Argentina"],
    [2, "Estados Unidos"],
    [3, "China"],
    [4, "Reino Unido"],
    [5, "Inglaterra"],
    [6, "Japon"],
    [7, "Otro"]
]     

class Producto(models.Model):
    rut_id = models.CharField(max_length=12)
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=30)
    comuna = models.CharField(max_length=30, default="")
    pais = models.IntegerField(choices=opciones_pais)
    telefono = models.CharField(max_length=10)
    moneda_pago = models.IntegerField(choices=opciones_moneda)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20, null=False)
    Tipo_Proveedor = models.ForeignKey(Marca, on_delete=models.PROTECT)     
    imagen = models.ImageField(default= "404.jpg", upload_to="productos", null=False)
    
    def __str__(self):
        return self.nombre

opciones_consulta = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_contacto = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre




