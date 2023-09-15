from django.shortcuts import render
from django.views import generic
from teachers.models import calification
from School.models import *
from django.contrib.auth.decorators import login_required,user_passes_test,permission_required
from datetime import datetime
from django.http import HttpResponse
from django.views import View
from reportlab.pdfgen import canvas
@login_required(login_url='/login')
@permission_required("students.view_history",login_url='/logout')
def estudiante(request):
    try:
        id = 0
        if request.session['id_estudiante'] is not None:
            id = request.session['id_estudiante']
        students = Students.objects.get(id= id)
        insc = Inscription.objects.all()
        
        for ins in insc:
            if ins.is_past_due == False and ins.student_id_id == id:
                inscription = ins
        #inscription_course = Inscription.objects.get(student_id=students.id)
        if inscription:
            subjects = Subject.objects.filter(level_id=inscription.course_id_id)
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
        insc = Inscription.objects.all()
        
        for ins in insc:
            if ins.is_past_due == False and ins.student_id_id == id:
                inscription = ins
                

        #inscription_course = Inscription.objects.get(student_id=inscription.student_id_id)
        
        print(inscription.student_id_id)
        if inscription:
            subjects = Subject.objects.filter(level_id=inscription.course_id_id)
            
            
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
        insc = Inscription.objects.all()
        
        for ins in insc:
            if ins.is_past_due == False and ins.student_id_id == id:
                inscription = ins
        #inscription_course = Inscription.objects.get(student_id=inscription.students_id_id)
        if inscription:
            subjects = Subject.objects.filter(level_id=inscription.course_id_id)
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
        insc = Inscription.objects.all()
        
        for ins in insc:
            if ins.is_past_due == False and ins.student_id_id == id:
                inscription = ins
        #inscription_course = Inscription.objects.get(student_id=inscription.student_id_id)
        if inscription:
            subjects = Subject.objects.filter(level_id=inscription.course_id_id)
            cali = calification.objects.filter(student_id_id=students.id)
            course = Course.objects.get(id=inscription.course_id_id)
            rel_teacher = Teacher_VS_Subjects.objects.all()
            teachers = Teachers.objects.all()
            edad = int((datetime.now().date() - students.birthdate).days / 365.25)
        return render(request,"informacion.html",{"subjects":subjects,"students":students,"cali":course,"teachers":teachers,"rel_teacher":rel_teacher,"edad":edad})  
    except:
        pass
    
    return render(request,"informacion.html")


from io import BytesIO
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import utils

def getpdf(request):
    # Obtén los datos de tu modelo (reemplaza 'MiModelo' con tu modelo real)
    try:
        id = 0
        if request.session.get('id_estudiante') is not None:
            id = request.session['id_estudiante']
            print(id)
    
        students = Students.objects.get(id=id)
        datos = calification.objects.filter(student_id_id=students.id)

    # Crea un objeto BytesIO para el PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="datos.pdf"'

    # Crea el PDF utilizando ReportLab
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)

        y =  800 # Posición vertical inicial

        for dato in datos:
            y -= 100
            p.drawString(100, y, f"ID Estudiante: {dato.student_id}")
            p.drawString(100, y - 15, f"Primer Periodo: {dato.firstPeriod}")
            p.drawString(100, y - 30, f"Segundo Periodo: {dato.secondPeriod}")
            p.drawString(100, y - 45, f"Tercer Periodo: {dato.thirdPeriod}")
            p.drawString(100, y - 60, f"Cuarto Periodo: {dato.fourthPeriod}")
            p.drawString(100, y - 75, f"Promedio: {dato.finish}")
        # Agrega más campos según tu modelo
            p.showPage()

        p.save()

        buffer.seek(0)
        response.write(buffer.read())
        buffer.close()
    
        return response
    except:
        pass