from django.shortcuts import render
from django.views import generic
from teachers.models import calification
from School.models import *
from django.contrib.auth.decorators import login_required,user_passes_test,permission_required

@login_required(login_url='/login')
@permission_required("students.view_history",login_url='/logout')
def lista_asignatura(request):
    try:
        id = 0
        if request.session['id_estudiante'] is not None:
            id = request.session['id_estudiante']
        students = Students.objects.get(id= id)
        inscription_course = Inscription.objects.get(student_id=students.id)
        if inscription_course:
            subjects = Subject.objects.filter(level_id=inscription_course.course_id_id)
            cali = calification.objects.all()
        return render(request,"estudiante_v2/index.html",{"subjects":subjects,"student":students,"cali":cali})  
    except:
        pass
    
    return render(request,"estudiante_v2/index.html")

def notes_list(request):
    califications=calification.objects.all()
    return render(request,"students/calification.html",{"calification":califications})
def students_list(request):
    students=Students.objects.all()
    return render(request,"students/students.html",{"student":students})
def subject_list(request):
    subjects=Subject.objects.all()
    return render(request,"students/calification.html",{"subjects":subjects})
