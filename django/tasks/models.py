from django.db import models

# --- MODELOS DEL TUTORIAL TASKFLOW ---

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "TODO", "Por hacer"
        IN_PROGRESS = "IN_PROGRESS", "En progreso"
        DONE = "DONE", "Completada"

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# --- MODELOS DE LA CLASE ---

class Sensei(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Mision(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Alumno(models.Model):
    sensei = models.ForeignKey(Sensei, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    edad = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    misiones = models.ManyToManyField(Mision, related_name='alumnos')

    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='perfiles/', blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.alumno.nombre}"

class Nave(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_nave = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Comida(models.Model):
    nombre_comida = models.CharField(max_length=100, default='Sin definir')
    categoria = models.CharField(max_length=100, default='Sin definir')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_comida
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre