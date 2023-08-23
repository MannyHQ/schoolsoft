from django.db import models

# Create your models here.
class asignatura(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateTimeField()
    descripcion = models.CharField(max_length=100)
    nivel = models.CharField(max_length=100)

class estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField()
    correo = models.CharField(max_length=100)
    telefono = models.IntegerField()
    estado = models.IntegerField()
    
class maestro(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)
    cedula = models.IntegerField()
    asignatura_id = models.ForeignKey(asignatura, on_delete=models.CASCADE)

class calificaciones(models.Model):
    estudiante_id = models.ForeignKey(estudiante, on_delete=models.CASCADE)
    asignatura_id = models.ForeignKey(asignatura, on_delete=models.CASCADE)
    maestro_id = models.ForeignKey(maestro, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    
class curso(models.Model):
    nivel = models.CharField(max_length=50)
    
class inscripcion(models.Model):
    id_estudiante = models.ForeignKey(estudiante, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField()
    estado_pago = models.IntegerField()
    ref_pago = models.IntegerField()
    estado_inscripcion = models.IntegerField()
    
class notas_maestros(models.Model):
    id_maestro = models.ForeignKey(maestro, on_delete=models.CASCADE)
    note = models.CharField(max_length=1000)
    

    
    
    
    