from django.contrib import admin
from .models import Project, ElearningEducacion, Comida, Nave

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(ElearningEducacion)
class ElearningAdmin(admin.ModelAdmin):
    list_display = ("educacion_basica", "educacion_superior", "created_at")
    search_fields = ("educacion_basica",)

@admin.register(Comida)
class ComidaAdmin(admin.ModelAdmin):
    list_display = ("__str__",) 

@admin.register(Nave)
class NaveAdmin(admin.ModelAdmin):
    list_display = ("__str__",) 