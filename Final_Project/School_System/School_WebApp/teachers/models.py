from django.db import models
from School.models import Students, Subject, Teachers, Inscription

class calification(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    firstPeriod = models.IntegerField(null=True)
    secondPeriod = models.IntegerField(null=True)
    thirdPeriod = models.IntegerField(null=True)
    fourthPeriod = models.IntegerField(null=True)
    finish = models.IntegerField(null=True)
    Subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)

class history_calification(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    firstPeriod = models.IntegerField(null=True)
    secondPeriod = models.IntegerField(null=True)
    thirdPeriod = models.IntegerField(null=True)
    fourthPeriod = models.IntegerField(null=True)
    finish = models.IntegerField(null=True)
    Subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)

class notes(models.Model):
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=1000)