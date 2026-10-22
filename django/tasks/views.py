from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """Vista de bienvenida de la app tasks."""
    return HttpResponse("""
        <html>
            <body>
                <h1>TaskFlow</h1>
                <p>Bienvenido al sistema</p>
            </body>
        </html>
    """)

def register(request):
    """Registro de usuarios"""
    return HttpResponse("Registro de Usuarios")

def about_me(request):
    """Registro de usuarios"""
    # Dejé tu línea original
    return HttpResponse("Tyron Ruilova<h1>Master</h1>")

def greeting(request, nombre):
    """Registro de usuarios"""
    return HttpResponse(f"Hola {nombre}, bienvenido a TaskFlow")

def destination(request, titulo, nombre, cargo):
    """Registro de usuarios"""
    return HttpResponse(f"Bienvenido: {titulo} {nombre}, su cargo es: {cargo}")

def base_triangulo(request, base, altura):
    """Registro de usuarios"""
    return HttpResponse(f"El área de un triángulo es: {base*altura/2}")

def my_firts_template(request, base, altura):
    """Registro de usuarios"""
    return HttpResponse(
        f"El área de un triángulo es: {base*altura/2}")

def my_first_template(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
    }
    return render(request, "tasks/my-first-template.html", contexto)

def leads_like(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
    }
    return render(request, "tasks/leads/leads-like.html", contexto)
def primera(request):
    return HttpResponse("Esta es mi primera vista")