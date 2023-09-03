from django.db import models
from teachers.models import calification
# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthdate = models.DateField()
    gender = models.CharField('genero',max_length=11)
    id_number = models.CharField('matricula',max_length=11)
    mail = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()
    status = models.SmallIntegerField()
class History(models.Model):
    student_id=models.ForeignKey(Students, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    Grade=models.CharField(max_length=50)
    asignature_id=models.IntegerField()
    note=models.ForeignKey(calification, on_delete=models.CASCADE)
    aprove=models.CharField(max_length=15)