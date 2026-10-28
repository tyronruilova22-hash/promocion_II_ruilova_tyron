from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
<<<<<<< HEAD
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Comida(models.Model):
    nombre = models.CharField(max_length=100)
    # ... tus otros campos

class Nave(models.Model):
    nombre = models.CharField(max_length=100)
    # ... tus otros campos

class ElearningEducacion(models.Model):
    educacion_basica = models.CharField(max_length=100)
    educacion_superior = models.CharField(max_length=100)
    educacion_complementaria = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.educacion_basica
=======
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ElearningEducacion(models.Model):
    educacion_basica = models.CharField(max_length=100)
    educacion_superior = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Comida(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Nave(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
>>>>>>> 80b56fafa1ae8884e9bfb7403cdb5c4960184166
