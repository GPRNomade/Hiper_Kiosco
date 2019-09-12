from rest_framework import serializers
from .models import producto

class productoModelSerializer(serializers.ModelSerializer): #tiene la misma estructura que el form
    class Meta:
        model = producto
        fields = [
                'id',  #para identificar de manera inequívoca
                'nombre_producto',
                'descripcion',
                'precio_sug_vta',
        ]

