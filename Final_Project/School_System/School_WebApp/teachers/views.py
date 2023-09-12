from django.shortcuts import render,redirect, get_object_or_404
from School.models import *
from .models import *
from .models import notes
from django.http import HttpResponse
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import request
from collections import defaultdict
from django.contrib.auth.decorators import login_required,user_passes_test,permission_required
from django.db.models import Max
from django.contrib import messages
from datetime import datetime
from django.db import transaction



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
                    
        # mensaje superior
        mensaje = ""
        # Comprobar la ruta actual
        if request.path == '/teachers/':
            mensaje = "Calificaciones destacadas de la institucion"
        elif request.path == '/courses/':
            mensaje = "Cursos y sus estudiantes a calificar"


        # Obtener todas las notas relacionadas con el profesor actual
        teacher_notes = notes.objects.filter(teacher_id=teacher_id)
        # Filtrar notas por título si se proporciona un título de búsqueda
        title_filter = request.GET.get('busqueda')
        if title_filter:
            teacher_notes = teacher_notes.filter(title__icontains=title_filter)

        if request.method == 'POST':
            # Obtener el id de la nota a eliminar desde el formulario
            note_id_to_delete = request.POST.get('note_id_to_delete')
            if note_id_to_delete:
                # Buscar y eliminar la nota por su id
                note_to_delete = get_object_or_404(notes, id=note_id_to_delete, teacher_id=teacher_id)
                note_to_delete.delete()
                return redirect('teachers')  # Redirigir de nuevo a la página de profesores

        return render(request, 'teachers/teachers.html', {'nombre': nombreTeacher, 'highest_scores': highest_scores, 'teacher_notes': teacher_notes, 'mensaje': mensaje})
    else:
        return redirect('login')

#---------notas personales-----------------
def notes_teacher(request):
    # nombreTeacher = request.session['profesor_nombre']    
    if request.method == 'POST':
        teacher_id = request.session['id_profesor']
        teacher_instance = Teachers.objects.get(id=teacher_id)
        new_note = notes(
             teacher_id = teacher_instance,
             title = request.POST['title_note'],
             note = request.POST['note'],
        )
        new_note.save()
        return redirect('teachers')
    else:
        return redirect('teachers')



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
            relationships = Teacher_VS_Subjects.objects.filter(teacher_id=teacher_id)
        
            if request.path == '/courses/':
                mensaje = "Cursos y sus estudiantes a calificar"
                
            for relationship in relationships:
                asignatura = relationship.subject_id
                course_id = asignatura.level_id
            
            # Encuentra todos los estudiantes asociados a esta asignatura y curso
                student_ids = Inscription.objects.filter(course_id=course_id).values_list('student_id', flat=True)
                from datetime import datetime
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
            fecha_actual = datetime.now().date()
            # print(fecha_actual)
            if relationships.exists():
                cursos_del_maestro = []
                cursos_visitados = set()  # To avoid duplicate courses
                
                for relationship in relationships:
                    subject = relationship.subject_id
                    curso = subject.level 

                    # Check if the course has already been visited
                    if curso.id not in cursos_visitados:
                        cursos_visitados.add(curso.id)  # Add the course to the visited set
                        
                        inscriptions = Inscription.objects.filter(course_id=curso.id)
                        students = set()
                        studentsExp = set()
                        
                        other_subjects = Subject.objects.filter(level_id=curso.id).exclude(id=subject.id)
                        
                        for inscription in inscriptions:
                            end_date = inscription.end_date
                            if end_date > fecha_actual:
                                students.add(inscription.student_id)
                            elif end_date < fecha_actual:
                                studentsExp.add(inscription.student_id)
                                for student_exp in studentsExp:
                                    # Get all subjects related to the student in the calification model
                                    related_subjects = calification.objects.filter(student_id=student_exp)
    
                                    for current_grade in related_subjects:
                                        # Check if a history_calification record already exists for this student and subject
                                        existe_history = history_calification.objects.filter(student_id=student_exp, Subject_id=current_grade.Subject_id).exists()
                                        
                                        if not existe_history:
                                            # If no history record exists, create a new one
                                            new_history = history_calification(
                                                firstPeriod=current_grade.firstPeriod,
                                                secondPeriod=current_grade.secondPeriod,
                                                thirdPeriod=current_grade.thirdPeriod,
                                                fourthPeriod=current_grade.fourthPeriod,
                                                finish=current_grade.finish,
                                                student_id=current_grade.student_id,
                                                Subject_id=current_grade.Subject_id,
                                            )
                                            new_history.save()
                                    
                        # other_subjects = Subject.objects.filter(level_id=curso.id).exclude(id=subject.id)

                        # Crear calificaciones para todas las asignaturas del curso
                        for other_subject in other_subjects:
                            for student in students:
                                # inscriptionEstud = Inscription.objects.filter( student_id = student)
                                existe_calificacion = calification.objects.filter(student_id=student,  Subject_id=asignatura).exists()
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
                            'asignatura': asignatura,
                            'students': list(students),
                        })
                # Redirigir de nuevo a la página de profesores
            return render(request, 'teachers/courses.html', {'cursos': cursos_del_maestro,'nombre': nombreTeacher, 'mensaje': mensaje})
        except:
            pass
        return render(request, 'teachers/courses.html')
    else:
        return redirect('login')

@login_required(login_url='/login')
@permission_required("teachers.view_calification",login_url='/logout')
#problema resuelto
def calificar(request):
    if 'profesor_nombre' in request.session and request.session['profesor_nombre']:
        try:
            nombreTeacher = request.session['profesor_nombre']
            teacher_id = request.session['id_profesor'] 
            student_id = request.POST.get('student_id')
            student_name = request.POST.get('student_name')
            
            if not student_id:
                student_id = request.session.get('student_id')
            if not student_name:
                student_name = request.session.get('student_name')
            
            student = get_object_or_404(Students, id=student_id)
            inscriptions = Inscription.objects.filter(student_id=student)
            related_subjects = Teacher_VS_Subjects.objects.filter(teacher_id=teacher_id)
            subject_ids = related_subjects.values_list('subject_id', flat=True)
            
            calificacion = calification.objects.filter(student_id=student, Subject_id_id__in=subject_ids)
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
            
            if request.path == '/calificar/':
                mensaje = "Estudiante a calificar en expecifico"
                
            return render(request, 'teachers/calification.html', {'student': student, 'cursos_y_asignaturas': cursos_y_asignaturas, 'list_calificaciones': list_calificaciones,'nombre': nombreTeacher, 'mensaje': mensaje})
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
            
            def validate_and_save_calification(calification_obj, value, field_name):
                try:
                    value = float(value)
                    if 0 <= value <= 100:
                        setattr(calification_obj, field_name, value)
                        calification_obj.save()
                    else:
                        messages.error(request, f'Dato no permitido en el campo "{field_name}"')
                except ValueError:
                    messages.error(request, f'Dato no permitido en el campo "{field_name}"')
                
            if 'button1' in request.POST:
                p1 = request.POST.get('p1')
                if p1.strip():
                    calificacion_obj, created = calification.objects.get_or_create(
                        student_id_id=student_id,
                        Subject_id_id=asignatura_id,
                        defaults={'firstPeriod': p1}
                    )
                    if not created:
                        validate_and_save_calification(calificacion_obj, p1, 'firstPeriod')
                return redirect('calificar')
            
            elif 'button2' in request.POST:
                p2 = request.POST.get('p2')
                if p2.strip():
                    calificacion_obj, created = calification.objects.get_or_create(
                        student_id_id=student_id,
                        Subject_id_id=asignatura_id,
                        defaults={'secondPeriod': p2}
                    )
                    if not created:
                        validate_and_save_calification(calificacion_obj, p2, 'secondPeriod')
                return redirect('calificar')
            
            elif 'button3' in request.POST:
                p3 = request.POST.get('p3')
                if p3.strip():
                    calificacion_obj, created = calification.objects.get_or_create(
                        student_id_id=student_id,
                        Subject_id_id=asignatura_id,
                        defaults={'thirdPeriod': p3}
                    )
                    if not created:
                        validate_and_save_calification(calificacion_obj, p3, 'thirdPeriod')
                return redirect('calificar')
            
            elif 'button4' in request.POST:
                p4 = request.POST.get('p4')
                if p4.strip():
                    calificacion_obj, created = calification.objects.get_or_create(
                        student_id_id=student_id,
                        Subject_id_id=asignatura_id,
                        defaults={'fourthPeriod': p4}
                    )
                    if not created:
                        validate_and_save_calification(calificacion_obj, p4, 'fourthPeriod')
                return redirect('calificar')
            
            elif 'button5' in request.POST:
                p5 = request.POST.get('p5')
                if p5.strip():
                    calificacion_obj, created = calification.objects.get_or_create(
                        student_id_id=student_id,
                        Subject_id_id=asignatura_id,
                        defaults={'finish': p5}
                    )
                    if not created:
                        validate_and_save_calification(calificacion_obj, p5, 'finish')
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
                        calificacion = calification.objects.filter(student_id=student, Subject_id=subject_id_filter).first()
                        asignatura_existe = calificacion is not None
                    else:
                        calificacion = calification.objects.filter(student_id=student, Subject_id=subject).first()
                        asignatura_existe = calificacion is not None

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
                        'asignatura_existe': asignatura_existe,
                    })



        if request.path == '/courses_califications/':
            mensaje = "Cursos y calificaciones segun las asignaturas y periodos"
                
        return render(request, 'teachers/calificationCourses.html', {'cursos': cursos_del_maestro, 'calification_filter': calification_filter,'nombre': nombreTeacher, 'mensaje': mensaje})
    else:
        return redirect('login')

            
            
        

    
        
    
    