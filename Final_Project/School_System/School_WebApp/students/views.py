from django.shortcuts import render
from django.views import generic
from teachers.models import calification
from School.models import *
from django.contrib.auth.decorators import login_required,user_passes_test,permission_required
from datetime import datetime
@login_required(login_url='/login')
@permission_required("students.view_history",login_url='/logout')
def estudiante(request):
    try:
        id = 0
        if request.session['id_estudiante'] is not None:
            id = request.session['id_estudiante']
        students = Students.objects.get(id= id)
        inscription_course = Inscription.objects.get(student_id=students.id)
        if inscription_course:
            subjects = Subject.objects.filter(level_id=inscription_course.course_id_id)
            cali = calification.objects.all()
        return render(request,"student.html",{"subjects":subjects,"students":students,"cali":cali})  
    except:
        pass
    
    return render(request,"student.html")

@login_required(login_url='/login')
@permission_required("students.view_history",login_url='/logout')
def ver_calificaciones(request):
    try:
        id = 0
        if request.session['id_estudiante'] is not None:
            id = request.session['id_estudiante']
            print(id)
        students = Students.objects.get(id= id)
        inscription_course = Inscription.objects.get(student_id=students.id)
        if inscription_course:
            subjects = Subject.objects.filter(level_id=inscription_course.course_id_id)
            
            
            cali = calification.objects.filter(student_id_id=students.id)
        return render(request,"calificaciones.html",{"subjects":subjects,"students":students,"cali":cali})  
    except:
        pass
    
    return render(request,"calificaciones.html")

@login_required(login_url='/login')
@permission_required("students.view_history",login_url='/logout')
def ver_asignaturas(request):
    try:
        id = 0
        if request.session['id_estudiante'] is not None:
            id = request.session['id_estudiante']
            print(id)
        students = Students.objects.get(id= id)
        inscription_course = Inscription.objects.get(student_id=students.id)
        if inscription_course:
            subjects = Subject.objects.filter(level_id=inscription_course.course_id_id)
            cali = calification.objects.filter(student_id_id=students.id)
            rel_teacher = Teacher_VS_Subjects.objects.all()
            teachers = Teachers.objects.all()
        return render(request,"asignaturas.html",{"subjects":subjects,"students":students,"cali":cali,"teachers":teachers,"rel_teacher":rel_teacher})  
    except:
        pass
    
    return render(request,"asignaturas.html")

@login_required(login_url='/login')
@permission_required("students.view_history",login_url='/logout')
def informacion(request):
    try:
        id = 0
        if request.session['id_estudiante'] is not None:
            id = request.session['id_estudiante']
            print(id)
        students = Students.objects.get(id= id)
        inscription_course = Inscription.objects.get(student_id=students.id)
        if inscription_course:
            subjects = Subject.objects.filter(level_id=inscription_course.course_id_id)
            cali = calification.objects.filter(student_id_id=students.id)
            course = Course.objects.get(id=inscription_course.course_id_id)
            rel_teacher = Teacher_VS_Subjects.objects.all()
            teachers = Teachers.objects.all()
            edad = int((datetime.now().date() - students.birthdate).days / 365.25)
        return render(request,"informacion.html",{"subjects":subjects,"students":students,"cali":course,"teachers":teachers,"rel_teacher":rel_teacher,"edad":edad})  
    except:
        pass
    
    return render(request,"informacion.html")