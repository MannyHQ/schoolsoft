from django.db import models
from School.models import Students, Subject

class calification(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    firstPeriod = models.IntegerField(null=True)
    secondPeriod = models.IntegerField(null=True)
    thirdPeriod = models.IntegerField(null=True)
    fourthPeriod = models.IntegerField(null=True)
    finish = models.IntegerField(null=True)
    Subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
 