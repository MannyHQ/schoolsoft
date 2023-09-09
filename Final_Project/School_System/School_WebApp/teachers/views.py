from django.shortcuts import render,redirect, get_object_or_404
from School.models import *
from .models import *
from django.http import HttpResponse
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import request
from collections import defaultdict
from django.contrib.auth.decorators import login_required,user_passes_test,permission_required
from django.db.models import Max



@login_required(login_url='/login')
#@user_passes_test(grupo_check,login_url='/login')
@permission_required("teachers.view_calification",login_url='/logout')
def teachers(request):
    if 'profesor_nombre' in request.session and request.session['profesor_nombre']:
        nombreTeacher = request.session['profesor_nombre']
        teacher_id = request.session['id_profesor']
        
        # Obtener las asignaturas enseñadas por el profesor
        subjects_taught = Teacher_VS_Subjects.objects.filter(teacher_id=teacher_id)

        # Diccionario para almacenar las calificaciones más altas por columna
        highest_scores = {}

        # Obtener las columnas de calificación que se deben consultar
        columns_to_query = ['firstPeriod', 'secondPeriod', 'thirdPeriod', 'fourthPeriod', 'finish']

        for column in columns_to_query:
            # Consultar la calificación máxima para la columna actual
            max_score = calification.objects.aggregate(Max(column))[f'{column}__max']

            if max_score is not None:
                # Buscar el estudiante y la asignatura relacionados con la calificación más alta
                student_data = calification.objects.filter(**{column: max_score}).first()

                if student_data:
                    subject_name = student_data.Subject_id.name
                    student_name = f"{student_data.student_id.first_name} {student_data.student_id.last_name}"

                    # Crear una entrada en el diccionario de calificaciones más altas
                    highest_scores[column] = {
                        'subject_name': subject_name,
                        'student_name': student_name,
                        'score': max_score,
                    }

        return render(request, 'teachers/teachers.html', {'nombre': nombreTeacher, 'highest_scores': highest_scores})
    else:
        return redirect('login')



#---------crear curso, asignatura y estudiante-------------
@login_required(login_url='/login')
@permission_required("teachers.view_calification",login_url='/logout')
def Creacion(request):
    return render(request, 'teachers/courses.html')

@login_required(login_url='/login')
@permission_required("teachers.view_calification",login_url='/logout')
def lista_curso(request):
    if 'profesor_nombre' in request.session and request.session['profesor_nombre']:
        try:
            nombreTeacher = request.session['profesor_nombre']
            teacher_id = request.session['id_profesor'] 
            print(teacher_id)
            relationships = Teacher_VS_Subjects.objects.filter(teacher_id=teacher_id)
        
            for relationship in relationships:
                asignatura = relationship.subject_id
                course_id = asignatura.level_id
            
            # Encuentra todos los estudiantes asociados a esta asignatura y curso
                student_ids = Inscription.objects.filter(course_id=course_id).values_list('student_id', flat=True)
            
                for student_id in student_ids:
                    student = Students.objects.get(id=student_id)  # Obtener la instancia del estudiante
                    existe_calificacion = calification.objects.filter(student_id=student, Subject_id=asignatura).exists()
                
                    if not existe_calificacion:
                        nueva_calificacion = calification(
                            student_id=student,  # Utilizar la instancia del estudiante
                            Subject_id=asignatura,
                            firstPeriod=None,
                            secondPeriod=None,
                            thirdPeriod=None,
                            fourthPeriod=None,
                            finish=None
                        )
                        nueva_calificacion.save()

            # cursos_del_maestro = []

            if relationships.exists():
                cursos_del_maestro = []
                cursos_visitados = set()  # Para evitar cursos duplicados
                
                for relationship in relationships:
                    subject = relationship.subject_id
                    curso = subject.level 
                    
                    # Verifica si el curso ya ha sido visitado
                    if curso.id not in cursos_visitados:
                        cursos_visitados.add(curso.id)  # Agrega el curso a los visitados
                        
                        inscriptions = Inscription.objects.filter(course_id=curso.id)
                        students = set()
                        
                        for inscription in inscriptions:
                            students.add(inscription.student_id)
                        
                        other_subjects = Subject.objects.filter(level_id=curso.id).exclude(id=subject.id)

                        # Crear calificaciones para todas las asignaturas del curso
                        for other_subject in other_subjects:
                            for student in students:
                                existe_calificacion = calification.objects.filter(student_id=student, Subject_id=other_subject).exists()
                                if not existe_calificacion:
                                    nueva_calificacion = calification(
                                        student_id=student,
                                        Subject_id=other_subject,
                                        firstPeriod=None,
                                        secondPeriod=None,
                                        thirdPeriod=None,
                                        fourthPeriod=None,
                                        finish=None
                                    )
                                    nueva_calificacion.save()
                        
                        
                        cursos_del_maestro.append({
                            'curso': curso,
                            'asignatura': subject,
                            'students': list(students),  # Convierte el conjunto en lista
                        })
            return render(request, 'teachers/courses.html', {'cursos': cursos_del_maestro,'nombre': nombreTeacher})
        except:
            pass
        return render(request, 'teachers/courses.html')
    else:
            return redirect('login')

@login_required(login_url='/login')
@permission_required("teachers.view_calification",login_url='/logout')
def calificar(request):
    if 'profesor_nombre' in request.session and request.session['profesor_nombre']:
        try:
            nombreTeacher = request.session['profesor_nombre']
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
                finish = califi.finish
                Subject_id = califi.Subject_id_id
                student_id_id = califi.student_id_id
                
                # Calculate finish based on non-empty values
                total_values = 0
                total_sum = 0

                if first is not None:
                    total_values += 1
                    total_sum += first
                if second is not None:
                    total_values += 1
                    total_sum += second
                if third is not None:
                    total_values += 1
                    total_sum += third
                if four is not None:
                    total_values += 1
                    total_sum += four

                finish = total_sum / total_values if total_values > 0 else None
                finish = round(finish, 2) if finish is not None else None
                # Actualizar el modelo de Calificación con el acabado calculado
                califi.finish = finish
                califi.save()
                # Busca el nombre de la asignatura utilizando el ID de asignatura
                subject = Subject.objects.get(id=subj_id)
                
                list_calificaciones.append({
                    'subject_name': subject.name,
                    'first': first,
                    'second': second,
                    'third': third,
                    'four': four,
                    'finish': finish,
                    'subject_califi': Subject_id,
                    'student_id_id': student_id_id
                })
                
            for inscription in inscriptions:
                course = inscription.course_id
                subject = Subject.objects.filter(level_id=course)
                cursos_y_asignaturas.append({'course': course, 'subject': subject})
                
                
            return render(request, 'teachers/calification.html', {'student': student, 'cursos_y_asignaturas': cursos_y_asignaturas, 'list_calificaciones': list_calificaciones,'nombre': nombreTeacher})
        except Exception as e:
            return redirect('teachers')
    else:
        return redirect('login')
    
@login_required(login_url='/login')
@permission_required("teachers.view_calification",login_url='/logout')
def califications(request):
    if 'profesor_nombre' in request.session and request.session['profesor_nombre']:
        nombreTeacher = request.session['profesor_nombre']
        
        if request.method == 'POST':
            asignatura_id = request.POST.get('asignatura_id')
            student_id = request.POST.get('student_id')
            student_name = request.POST.get('student_name')
            
            request.session['student_id'] = student_id
            request.session['student_name'] = student_name
            
            if 'button1' in request.POST:
                p1 = request.POST.get('p1')
                if p1.strip():  # Verificar que el campo no esté en blanco
                    calificacion_obj, created = calification.objects.get_or_create(
                        student_id_id=student_id,
                        Subject_id_id=asignatura_id,
                        defaults={'firstPeriod': p1}
                    )
                    if not created:
                        calificacion_obj.firstPeriod = p1
                        calificacion_obj.save()
                return redirect('calificar')
            
            elif 'button2' in request.POST:
                p2 = request.POST.get('p2')
                if p2.strip():  # Verificar que el campo no esté en blanco
                    calificacion_obj, created = calification.objects.get_or_create(
                        student_id_id=student_id,
                        Subject_id_id=asignatura_id,
                        defaults={'secondPeriod': p2}
                    )
                    if not created:
                        calificacion_obj.secondPeriod = p2
                        calificacion_obj.save()
                return redirect('calificar')
            
            elif 'button3' in request.POST:
                p3 = request.POST.get('p3')
                if p3.strip():  # Verificar que el campo no esté en blanco
                    calificacion_obj, created = calification.objects.get_or_create(
                        student_id_id=student_id,
                        Subject_id_id=asignatura_id,
                        defaults={'thirdPeriod': p3}
                    )
                    if not created:
                        calificacion_obj.thirdPeriod = p3
                        calificacion_obj.save()
                return redirect('calificar')
            
            elif 'button4' in request.POST:
                p4 = request.POST.get('p4')
                if p4.strip():  # Verificar que el campo no esté en blanco
                    calificacion_obj, created = calification.objects.get_or_create(
                        student_id_id=student_id,
                        Subject_id_id=asignatura_id,
                        defaults={'fourthPeriod': p4}
                    )
                    if not created:
                        calificacion_obj.fourthPeriod = p4
                        calificacion_obj.save()
                return redirect('calificar')
            
            elif 'button5' in request.POST:
                p5 = request.POST.get('p5')
                if p5.strip():  # Verificar que el campo no esté en blanco
                    calificacion_obj, created = calification.objects.get_or_create(
                        student_id_id=student_id,
                        Subject_id_id=asignatura_id,
                        defaults={'finish': p5}
                    )
                    if not created:
                        calificacion_obj.finish = p5
                        calificacion_obj.save()
                return redirect('calificar', {'nombre': nombreTeacher})
                
        return redirect('calificar')
    else:
        return redirect('login')
@login_required(login_url='/login')
@permission_required("teachers.view_calification",login_url='/logout')
def teacher_course_califications(request):
    if 'profesor_nombre' in request.session and request.session['profesor_nombre']:
        nombreTeacher = request.session['profesor_nombre']
        teacher_id = request.session['id_profesor']   
        relationships = Teacher_VS_Subjects.objects.filter(teacher_id=teacher_id)
        cursos_del_maestro = []
        
        course_filter = request.POST.get('course')
        subject_filter = request.POST.get('subject')
        calification_filter = int(request.POST.get('calification', 0))
        subject_id_filter = None

        if subject_filter:
            # Buscar la asignatura por nombre en la tabla Subject
            subject_id_filter = Subject.objects.filter(name=subject_filter).values_list('id', flat=True).first()

        if relationships.exists():
            cursos_visitados = set()  # Para evitar cursos duplicados
            
            for relationship in relationships:
                subject = relationship.subject_id
                curso = subject.level 
                
                # Verifica si el curso ya ha sido visitado
                if curso.id not in cursos_visitados:
                    cursos_visitados.add(curso.id)  # Agrega el curso a los visitados
                    
                    inscriptions = Inscription.objects.filter(course_id=curso.id)
                    students = set()
                    
                    for inscription in inscriptions:
                        students.add(inscription.student_id)
                
                    # Obtener las calificaciones para cada estudiante en esta materia y curso
                    calificaciones_estudiantes = []
                    for student in students:
                        if subject_id_filter:
                            # Filtrar por la ID de asignatura si se proporciona en el formulario
                            calificacion = calification.objects.filter(student_id=student, Subject_id=subject_id_filter).first()
                        else:
                            # Si no se proporciona la ID de asignatura, utilizar la asignatura actual
                            calificacion = calification.objects.filter(student_id=student, Subject_id=subject).first()
                            
                        calificaciones_estudiantes.append({
                            'student': student,
                            'calificacion': calificacion
                        })

                    if course_filter and curso.level != course_filter:
                        continue
                    
                    if subject_id_filter:
                        # Si se proporciona la ID de asignatura, utilizarla para mostrar la asignatura
                        subject = Subject.objects.get(id=subject_id_filter)

                    # Filtrar por calificación si se proporciona en el formulario
                    if calification_filter:
                        # Convierte el valor de calification_filter a un campo de calificación
                        if calification_filter == 1:
                            field_filter = 'firstPeriod'
                        elif calification_filter == 2:
                            field_filter = 'secondPeriod'
                        elif calification_filter == 3:
                            field_filter = 'thirdPeriod'
                        elif calification_filter == 4:
                            field_filter = 'fourthPeriod'
                        elif calification_filter == 5:
                            field_filter = 'finish'
                        else:
                            field_filter = None
                                
                    cursos_del_maestro.append({
                        'curso': curso,
                        'asignatura': subject,
                        'calificaciones_estudiantes': calificaciones_estudiantes,
                    })

        return render(request, 'teachers/calificationCourses.html', {'cursos': cursos_del_maestro, 'calification_filter': calification_filter,'nombre': nombreTeacher})
    else:
        return redirect('login')
            
            
        

    
        
    
    