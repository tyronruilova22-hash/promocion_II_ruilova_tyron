from django.contrib import admin
from .models import Project, ElearningEducacion

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(ElearningEducacion)
class ElearningAdmin(admin.ModelAdmin):
    list_display = ("educacion_basica", "educacion_superior", "created_at")
    search_fields = ("educacion_basica",)