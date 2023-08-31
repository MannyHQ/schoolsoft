from django.db import models
from django.contrib.auth.models import User

class StudentUser(models.Model):
    id_number = models.CharField('matricula',max_length=11)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name="sur")

class ParentUser(models.Model):
    id_number = models.CharField('cedula',max_length=11)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name="pur")
    
class TeacherUser(models.Model):
    id_number = models.CharField('cedula',max_length=11)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name="tur")

class Students(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthdate = models.DateField()
    gender = models.CharField('genero',max_length=11)
    id_number = models.CharField('matricula',max_length=11)
    mail = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()
    status = models.SmallIntegerField()
    
class Course(models.Model):
    level = models.CharField(max_length=200)
    
class Subject(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    description = models.CharField(max_length=200)
    level = models.ForeignKey(Course, on_delete=models.CASCADE,)
    # level = models.IntegerField()
    
    def __str__(self):
        return self.name+' Curso:' + self.level

class Teachers(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    code = models.IntegerField()
    mail = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()
    id_number = models.CharField('cedula',max_length=11)
    status = models.SmallIntegerField()
    #subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Teacher_VS_Subjects(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE,)
    teacher_id =  models.ForeignKey(Teachers, on_delete=models.CASCADE,)
    def __str__(self):
        return f"ID: {self.subject_id.id}-{self.subject_id.name} Curso:{self.subject_id.level}"

class Parents(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    id_number = models.CharField('cedula',max_length=11)
    mail = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()
    status = models.SmallIntegerField()

class Inscription(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE,related_name="ist")
    course_id =  models.ForeignKey(Course, on_delete=models.CASCADE,related_name="ics")
    date_inscription = models.DateTimeField()
    start_date = models.DateField()
    end_date = models.DateField()
    inscription_status = models.SmallIntegerField()
    
    def __str__(self):
        return self.name+' Descripcion:'+self.description+' Curso:' + self.level
    

# Subject.level = models.ManyToManyField(Course, related_name='course')
