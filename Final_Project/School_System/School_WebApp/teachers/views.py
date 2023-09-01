from django.shortcuts import render,redirect, get_object_or_404
from School.models import *
from .models import *
from django.http import HttpResponse
from django.db.models import Count
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def teachers(request):
    return render(request, 'teachers/teachers.html')
#---------crear curso, asignatura y estudiante-------------
def Creacion(request):
    return render(request, 'teachers/courses.html')
    
def lista_curso(request):
    # Supongamos que tienes el ID del maestro que quieres consultar
    teacher_id = 1  

    # Encuentra todas las relaciones del maestro con cursos
    relationships = Teacher_VS_Subjects.objects.filter(teacher_id=teacher_id)
    
    for relacion in relationships:
            asignatura = relacion.subject_id
            maestro = Students.objects.get(id=1)
            existe_calificacion = calification.objects.filter(student_id=maestro, Subject_id=asignatura).exists()
            if not existe_calificacion:
                # Si no existe, crea una nueva calificación para la asignatura
                nueva_calificacion = calification(
                    student_id=maestro,
                    Subject_id=asignatura,
                    firstPeriod=None,  # Aquí debes establecer los valores adecuados
                    secondPeriod=None,
                    thirdPeriod=None,
                    fourthPeriod=None,
                    finish=None
                )
                nueva_calificacion.save()
        
    # print(arreglo)
    cursos_del_maestro = {}  # Usamos un diccionario para almacenar cursos únicos

    if relationships.exists():
        for relationship in relationships:
            subject = relationship.subject_id
            var = subject
            curso = subject.level  # Suponiendo que level almacena un objeto de curso
            # Obtener las inscripciones para este curso por su ID
            inscriptions = Inscription.objects.filter(course_id=curso.id)
            students = set()  # Usamos un conjunto para evitar duplicaciones

            for inscription in inscriptions:
                students.add(inscription.student_id)

            # Agregamos el curso y estudiantes al diccionario
            if curso.id not in cursos_del_maestro:
                cursos_del_maestro[curso.id] = {
                    'curso': curso,
                    'students': students,
                    'asignaturas': [subject.name],
                }
            else:
                cursos_del_maestro[curso.id]['students'].update(students)
                cursos_del_maestro[curso.id]['asignaturas'].append(subject.name)

    # Convertimos el conjunto de estudiantes en una lista antes de pasarlo a la plantilla
    for curso_info in cursos_del_maestro.values():
        curso_info['students'] = list(curso_info['students'])

    # Convertimos el diccionario en una lista antes de pasarlo a la plantilla
    cursos_del_maestro = list(cursos_del_maestro.values())

    return render(request, 'teachers/courses.html', {'cursos': cursos_del_maestro})



def calificar(request):
    try:
        student_id = request.POST.get('student_id')
        student_name = request.POST.get('student_name')
        
        # print(student_id+' '+student_name)
        if not student_id:
            student_id = request.session.get('student_id')
        if not student_name:
            student_name = request.session.get('student_name')
        
        
        student = get_object_or_404(Students, id=student_id)
        # relaciones = Teacher_VS_Subjects.objects.filter(teacher_id=1)
        inscriptions = Inscription.objects.filter(student_id=student)
        calificacion = calification.objects.filter(student_id=student)
        list_calificaciones = []
        cursos_y_asignaturas = []
        
        request.session.pop('student_id', None)
        request.session.pop('student_name', None)
        
        
        for califi in calificacion:
            subj_id = califi.Subject_id_id
            first = califi.firstPeriod
            second = califi.secondPeriod
            third = califi.thirdPeriod
            four = califi.fourthPeriod
            Subject_id = califi.Subject_id_id
            student_id_id = califi.student_id_id
            # Busca el nombre de la asignatura utilizando el ID de asignatura
            subject = Subject.objects.get(id=subj_id)
            
            list_calificaciones.append({
                'subject_name': subject.name,
                'first': first,
                'second': second,
                'third': third,
                'four': four,
                'subject_califi': Subject_id,
                'student_id_id': student_id_id
            })
            
        for inscription in inscriptions:
            course = inscription.course_id
            subject = Subject.objects.filter(level=course)
            cursos_y_asignaturas.append({'course': course, 'subject': subject})
            
            
        return render(request, 'teachers/calification.html', {'student': student, 'cursos_y_asignaturas': cursos_y_asignaturas, 'list_calificaciones': list_calificaciones})
    except Exception as e:
        return redirect('/teachers')

def califications(request):
    if request.method == 'POST':
        
        asignatura_id = request.POST.get('asignatura_id')
        student_id = request.POST.get('student_id')
        student_name = request.POST.get('student_name')
        
        request.session['student_id'] = student_id
        request.session['student_name'] = student_name
        
        if 'button1' in request.POST:
            p1 = request.POST.get('p1')
            
            calificacion_obj, created = calification.objects.get_or_create(
                student_id_id=student_id,
                Subject_id_id=asignatura_id,
                defaults={'firstPeriod': p1}
            )
            
            if not created:
                calificacion_obj.firstPeriod = p1
                calificacion_obj.save()
            return redirect('/calificar')
        
        elif 'button2' in request.POST:
            p2 = request.POST.get('p2')
            
            calificacion_obj, created = calification.objects.get_or_create(
                student_id_id=student_id,
                Subject_id_id=asignatura_id,
                defaults={'secondPeriod': p2}
            )
            
            if not created:
                calificacion_obj.secondPeriod = p2
                calificacion_obj.save()
            return redirect('/calificar')
        
        elif 'button3' in request.POST:
            p3 = request.POST.get('p3')
            
            calificacion_obj, created = calification.objects.get_or_create(
                student_id_id=student_id,
                Subject_id_id=asignatura_id,
                defaults={'secondPeriod': p3}
            )
            
            if not created:
                calificacion_obj.thirdPeriod = p3
                calificacion_obj.save()
            return redirect('/calificar')
        
        elif 'button4' in request.POST:
            p4 = request.POST.get('p4')
            
            calificacion_obj, created = calification.objects.get_or_create(
                student_id_id=student_id,
                Subject_id_id=asignatura_id,
                defaults={'secondPeriod': p4}
            )
            
            if not created:
                calificacion_obj.fourthPeriod = p4
                calificacion_obj.save()
            return redirect('/calificar')
        
        elif 'button5' in request.POST:
            p5 = request.POST.get('p5')
            
            calificacion_obj, created = calification.objects.get_or_create(
                student_id_id=student_id,
                Subject_id_id=asignatura_id,
                defaults={'secondPeriod': p5}
            )
            
            if not created:
                calificacion_obj.finish = p5
                calificacion_obj.save()
            return redirect('/calificar')
        
    return redirect('/calificar')
