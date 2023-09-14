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


from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from reportlab.pdfgen import canvas

class GenerarPDFView(View):
    def get(self, request):
        # Obtén los datos de tu modelo (reemplaza 'MiModelo' con tu modelo real)
        datos = calification.objects.all()

        # Crea un objeto BytesIO para el PDF
        response = HttpResponse(content_type='students/pdf')
        response['Content-Disposition'] = 'attachment; filename="datos.pdf"'

        # Crea el PDF utilizando ReportLab
        p = canvas.Canvas(response)  # Personaliza según tus datos
        y = 900  # Posición vertical inicial
        for dato in datos:
            y -= 100
            p.drawString(100, y, f"Campo 1: {dato.student_id}")
            p.drawString(100, y - 15, f"Campo 2: {dato.firstPeriod}")
            p.drawString(100, y - 30, f"Campo 3: {dato.secondPeriod}")
            p.drawString(100, y - 45, f"Campo 4: {dato.thirdPeriod}")
            p.drawString(100, y - 60, f"Campo 5: {dato.fourthPeriod}")
            p.drawString(100, y - 75, f"Campo 6: {dato.finish}")
            # Agrega más campos según tu modelo

        p.showPage()
        p.save()
        return response