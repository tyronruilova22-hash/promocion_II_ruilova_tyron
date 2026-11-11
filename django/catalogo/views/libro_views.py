from django.shortcuts import render
from ..models import Libro

def lista_libros(request):
    libros = Libro.objects.all()
    contexto = {
        'libros': libros
    }
    return render(request, 'catalogo/libros/lista_libros.html', contexto)
