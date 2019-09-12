from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import producto
from .serializers import productoModelSerializer
# Create your views here.



class productoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all() #
    serializer_class = productoModelSerializer

    