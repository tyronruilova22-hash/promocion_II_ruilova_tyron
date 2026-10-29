from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm
from .models import Project, Task

def home(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
        "projects": Project.objects.order_by("-created_at"),
    }
    return render(request, "home.html", contexto)

def register(request):
    return HttpResponse("Registro de Usuarios")

def about_me(request):
    return HttpResponse("Ing. Francisco Higuera")

def greeting(request, nombre):
    return HttpResponse(f"Hola {nombre}, bienvenido a TaskFlow")

def destination(request, titulo, nombre, cargo):
    return HttpResponse(f"Bienvenido: {titulo} {nombre}, su cargo es: {cargo}")

def base_triangulo(request, base, altura):
    return HttpResponse(f"El área de un triángulo es: {base*altura/2}")

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

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:home")
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form, "modo": "crear"})