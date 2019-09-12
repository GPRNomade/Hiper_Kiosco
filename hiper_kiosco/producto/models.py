from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

class producto(models.Model):
    #nombre, descripcion, codigo de producto(unico) y precio sugerido de venta(+)
    nombre_producto = models.CharField("Nombre de Producto", max_length=50, blank=False, null=False)
    descripcion = models.TextField("Descripción", blank=False, null=True)
    precio_sug_vta = models.DecimalField(("Precio sugerido de Venta"), blank=False, null=False, validators= [MinValueValidator(0, message="El precio debe ser mayor a $0")], max_digits=5, decimal_places=2)


    def __str__(self):
        return self.nombre_producto

