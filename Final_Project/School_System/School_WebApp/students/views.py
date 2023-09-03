from django.shortcuts import render
from django.views import generic
from teachers.models import calification
from School.models import *
# Create your views here.


def lista_asignatura(request):
    students = Students.objects.get(id=1)
    inscription_course = Inscription.objects.get(student_id=students.id)
    if inscription_course:
        subjects = Subject.objects.filter(level_id=inscription_course.course_id_id)
        cali = calification.objects.all()
        
        
        
    
    return render(request,"estudiante_v2/index.html",{"subjects":subjects,"student":students,"cali":cali})

def notes_list(request):
    califications=calification.objects.all()
    return render(request,"students/calification.html",{"calification":califications})
def students_list(request):
    students=Students.objects.all()
    return render(request,"students/students.html",{"student":students})
def subject_list(request):
    subjects=Subject.objects.all()
    return render(request,"students/calification.html",{"subjects":subjects})
