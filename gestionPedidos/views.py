from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos 

# Create your views here.

def busqueda_productos(request):

    return render(request, "busqueda_productos.html")

def buscar (request):

    if request.GET["prd"]:

        #mensaje="Articulo buscado: %r " %request.GET["prd"]
        producto=request.GET["prd"]

        if len(producto)>20:

            mensaje="Texto de busqueda largo"

        else:

            articulos=Articulos.objects.filter(nombre__icontains=producto)

            return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})
    else:
        
        mensaje="no se ingreso ningun valor"

    return HttpResponse(mensaje)

def contacto (request):
    return render(request, "contacto.html")