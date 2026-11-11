from django.urls import path
from ..views import libro_views

urlpatterns = [
    path('libros/', libro_views.lista_libros, name='libro_list'),
]
