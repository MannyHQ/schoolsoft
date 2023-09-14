from django.shortcuts import get_object_or_404,render,redirect
from .models import Students,Teachers,Parents,Subject,Course,Inscription
from django.http import HttpResponse
from django.template import loader
from School.forms import *
from School.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q,Sum
from django.contrib.auth.models import Group
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from datetime import datetime
from django.utils import timezone
def logout_view(request):
    logout(request)
    return redirect('/login')

@login_required(login_url="/login")
@staff_member_required
def assign_student_user(request):
    unassigned_users = UnassignedUser.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        identification = request.POST.get('identification')

        
        
        try:
            user = User.objects.get(username=username)
            student = Students.objects.get(id_number=identification)

            # Verificar si el usuario ya está asignado
            if not StudentUser.objects.filter(student_id=student, user_id=user).exists():
                # Asignar el usuario al estudiante
                student_user, created = StudentUser.objects.get_or_create(student_id=student, user_id=user)

                if created:
                    # Crear una instancia de UnassignedUser para el usuario asignado
                    UnassignedUser.objects.filter(user=user).delete()
                    
                    # Asignar al usuario al grupo de estudiantes
                    group = Group.objects.get(name='Estudiante')  # Reemplaza 'Estudiantes' con el nombre de tu grupo de estudiantes
                    user.groups.add(group)
                    messages.success(request,'Usuario asignado correctamente!')
                return redirect('/home')  # Redirigir a la lista de estudiantes

        except User.DoesNotExist:
            messages.error(request,'El usuario no existe!')
            return render(request, 'School/assign-user.html', {'error_message': 'El nombre de usuario no existe.', 'unassigned_users': unassigned_users})
        except Students.DoesNotExist:
            messages.error(request,'No se encontró al estudiante!')
            return render(request, 'School/assign-user.html', {'error_message': 'No se encontró al estudiante con esta matrícula.', 'unassigned_users': unassigned_users})

    return render(request, 'School/assign-user.html', {'form': AssignUserForm(), 'unassigned_users': unassigned_users})

@login_required(login_url="/login")
@staff_member_required
def assign_teacher_user(request):
    unassigned_users = UnassignedUser.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        identification = request.POST.get('identification')

        
        
        try:
            user = User.objects.get(username=username)
            teacher = Teachers.objects.get(id_number=identification)

            # Verificar si el usuario ya está asignado
            if not TeacherUser.objects.filter(teacher_id=teacher, user_id=user).exists():
                # Asignar el usuario al estudiante
                teacher_user, created = TeacherUser.objects.get_or_create(teacher_id=teacher, user_id=user)

                if created:
                    # Crear una instancia de UnassignedUser para el usuario asignado
                    UnassignedUser.objects.filter(user=user).delete()
                    
                    # Asignar al usuario al grupo de estudiantes
                    group = Group.objects.get(name='Profesor')  # Reemplaza 'Profesores' con el nombre de tu grupo de estudiantes
                    user.groups.add(group)
                    messages.success(request,'Usuario asignado correctamente')
                return redirect('/home')  # Redirigir a la lista de profesores

        except User.DoesNotExist:
            messages.error(request,'Usuario no existe!')
            return render(request, 'School/assign-user2.html', {'error_message': 'El nombre de usuario no existe.', 'unassigned_users': unassigned_users})
        except Teachers.DoesNotExist:
            messages.error(request,'No se encontró al profesor!')
            return render(request, 'School/assign-user2.html', {'error_message': 'No se encontró al estudiante con esta matrícula.', 'unassigned_users': unassigned_users})

    return render(request, 'School/assign-user2.html', {'form': AssignUserForm(), 'unassigned_users': unassigned_users})

@login_required(login_url="/login")
@staff_member_required
def assign_parent_user(request):
    unassigned_users = UnassignedUser.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        identification = request.POST.get('identification')

        
        
        try:
            user = User.objects.get(username=username)
            parent = Parents.objects.get(id_number=identification)

            # Verificar si el usuario ya está asignado
            if not ParentUser.objects.filter(parent_id=parent, user_id=user).exists():
                # Asignar el usuario al estudiante
                parent_user, created = ParentUser.objects.get_or_create(parent_id=parent, user_id=user)

                if created:
                    # Crear una instancia de UnassignedUser para el usuario asignado
                    UnassignedUser.objects.filter(user=user).delete()
                    
                    # Asignar al usuario al grupo de estudiantes
                    group = Group.objects.get(name='Padre')  # Reemplaza 'Padres' con el nombre de tu grupo de estudiantes
                    user.groups.add(group)
                    
                return redirect('/home')  # Redirigir a la lista de Padres

        except User.DoesNotExist:
            return render(request, 'School/assign-user3.html', {'error_message': 'El nombre de usuario no existe.', 'unassigned_users': unassigned_users})
        except Students.DoesNotExist:
            return render(request, 'School/assign-user3.html', {'error_message': 'No se encontró al estudiante con esta matrícula.', 'unassigned_users': unassigned_users})

    return render(request, 'School/assign-user3.html', {'form': AssignUserForm(), 'unassigned_users': unassigned_users})



def login_us(request):
    username = ""
    password = ""
    template = "School/page-login.html"

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username = username,password = password)
        
        if user is not None and user.is_staff == True and user.is_active:
            login(request,user)
            return redirect('/home')
        elif user is not None and user.is_staff == False:
            grupo = list(user.groups.values_list('name',flat=True))
            grupo_valor = ''.join(grupo)
            request.session['staff'] = user.is_staff
            try:
                if grupo_valor == 'Estudiante':
                    print("Es estudiante")
                    student_user=StudentUser.objects.get(user_id_id=user.id)
                    student_profile = Students.objects.get(id=student_user.student_id_id)
                    nombre = student_profile.first_name+' '+student_profile.last_name
                    request.session['estudiante_nombre'] = nombre
                    request.session['id_estudiante'] = student_profile.id
                    request.session['usuario'] = user.username
                    
                    login(request,user)
                    return redirect('/student')
                elif grupo_valor == 'Profesor':
                    print('Es profesor')
                    profesor_user=TeacherUser.objects.get(user_id_id=user.id)
                    profesor_profile = Teachers.objects.get(id=profesor_user.teacher_id_id)
                    nombre = profesor_profile.first_name+' '+profesor_profile.last_name
                    request.session['profesor_nombre'] = nombre
                    request.session['id_profesor'] = profesor_profile.id
                    request.session['usuario'] = user.username
                    
                    login(request,user)
                    return redirect('/teachers')
                elif grupo_valor == 'Padre':
                    print('Es padre')
            except:
                pass
            
            #print(list(user.groups.values_list('name',flat=True)))
        else:
            messages.error(request,'Credenciales incorrectas!')
            return render(request,template)
        
    return render(request,template)

@login_required(login_url="/login")
@staff_member_required
def index(request):
    students_count = Students.objects.count()
    courses_count = Course.objects.count()
    teachers_count = Teachers.objects.count()
    inscription_count = Inscription.objects.count()
    subjects_count = Subject.objects.count()
    users_count = User.objects.count()
    parents_count = Parents.objects.count()
    bill_sum = Pagos.objects.aggregate(Sum('monto_total'))
    try:
        monthly_pay = Cobro.objects.all()[:1]
    except:
        monthly_pay = {'mensualidad': 0}
        pass
    latest_inscriptions_list = Inscription.objects.order_by("-date_inscription")[:5]
    template = loader.get_template("school/index.html")
    context = {
        "latest_inscriptions_list": latest_inscriptions_list,
        "students_count": students_count,
        'courses_count':courses_count,
        'teachers_count':teachers_count,
        'inscription_count':inscription_count,
        'bill_sum': bill_sum,
        'subjects_count': subjects_count,
        'users_count': users_count,
        'parents_count': parents_count,
        'monthly_pay': monthly_pay,
    }
    
    return HttpResponse(template.render(context,request))

@login_required(login_url="/login")
@staff_member_required
def all_professors(request):
    teachers = Teachers.objects.all()
    return render(request,'School/all-professors.html',{'teachers':teachers})

@login_required(login_url="/login")
@staff_member_required
def all_students(request):
    students = Students.objects.all()
    return render(request,'School/all-students.html',{'students':students})

@login_required(login_url="/login")
@staff_member_required
def all_courses(request):
    courses = Course.objects.all()
    return render(request,'School/all-courses.html',{'courses':courses})

@login_required(login_url="/login")
@staff_member_required
def lista_pagos(request):
    pagos = Pagos.objects.all()
    padres = Parents.objects.all()
    estudiantes = Students.objects.all()
    return render(request,'School/lista-pagos.html',{'pagos':pagos,'padres':padres,'estudiantes':estudiantes})


@login_required(login_url="/login")
@staff_member_required
def all_parents(request):
    parents = Parents.objects.all()
    return render(request,'School/all-departments.html',{'parents':parents})

@login_required(login_url="/login")
@staff_member_required
def all_subjects(request):
    subjects = Subject.objects.all()
    return render(request,'School/all-library.html',{'subjects':subjects})

@login_required(login_url="/login")
@staff_member_required
def all_staff(request):
    staff = User.objects.all()
    return render(request,'School/all-staff.html',{'staff':staff})

@login_required(login_url="/login")
@staff_member_required
def all_inscription(request):
    inscription = Inscription.objects.all()
    return render(request,'School/all-inscriptions.html',{'inscription':inscription})




@login_required(login_url="/login")
@staff_member_required
def asignar_asignaturas(request, profesor_id):
    if request.method == 'POST':
        form = TeacherSubjectForm(request.POST)
        if form.is_valid():
            profesor = Teachers.objects.get(pk=profesor_id)
            for asignatura in form.cleaned_data['asginaturas']:
                Teacher_VS_Subjects.objects.create(teacher_id=profesor, subject_id=asignatura)
            messages.success(request,'Asignatura asignada correctamente!')
            return redirect('/home')
    else:
        messages.error(request,'Hubo un error al asignar la asignatura!')
        form = TeacherSubjectForm()
    return render(request, 'School/assign_subject.html', {'form': form})

@login_required(login_url="/login")
@staff_member_required
def quitar_asignaturas(request, profesor_id):
    profesor = get_object_or_404(Teachers, pk=profesor_id)

    if request.method == 'POST':
        asignatura_id = request.POST.get('asignatura_id')
        asignatura = get_object_or_404(Subject, pk=asignatura_id)
        Teacher_VS_Subjects.objects.filter(subject_id=asignatura, teacher_id=profesor).delete()
        return redirect('/remove-subject/{profesor_id}')

    asignaturas_asignadas = profesor.teacher_vs_subjects_set.all()
    return render(request, 'School/template.html', {'profesor': profesor, 'asignaturas_asignadas': asignaturas_asignadas})

@login_required(login_url="/login")
@staff_member_required
def desasignar_asignaturas(request, profesor_id):
    profesor = get_object_or_404(Teachers, pk=profesor_id)
    asignaturas_asignadas = profesor.teacher_vs_subjects_set.all()

    if request.method == 'POST':
        asignaturas_desasignar_ids = request.POST.getlist('asignaturas_desasignar')
        asignaturas_desasignar = Subject.objects.filter(id__in=asignaturas_desasignar_ids)
        profesor.teacher_vs_subjects_set.filter(subject_id__in=asignaturas_desasignar).delete()
        messages.success(request,'Asignaturas desasignadas correctamente!')
        return redirect('/home')

    return render(request, 'School/desasignar_asignaturas_tabla.html', {'profesor': profesor, 'asignaturas_asignadas': asignaturas_asignadas})







@login_required(login_url="/login")
@staff_member_required
def select_professor(request):
    teachers = Teachers.objects.all()
    template = "School/select_teacher.html"
    return render(request,template,{'teachers':teachers})

def select_student(request):
    students = Students.objects.all()
    template = "School/select_student.html"
    return render(request, template,{'students':students})

@login_required(login_url="/login")
@staff_member_required
def add_courses(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'Curso agregado correctamente!')
                return redirect('/add-courses')
            except:
                messages.error(request,'Error al agregar un curso!')
                pass
    else:
        form = CourseForm()
    return render(request,'School/add-courses.html',{'form': form})

@login_required(login_url="/login")
@staff_member_required
def add_mensualidad(request):
    if request.method == 'POST':
        form = CobroForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'Mensualidad agregada correctamente!')
                return redirect('/mensualidad')
            except:
                messages.error(request,'Error al agregar la mensualidad!')
                pass
    else:
        form = CobroForm()
    return render(request,'School/tarifa.html',{'form': form})

@login_required(login_url="/login")
@staff_member_required
def crear_usuario_padre(request):
    parents = Parents.objects.all()
    print(request.POST)
    if request.method == "POST":
        form = PadreUserForm(request.POST)
        form.save()
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'Usuario padre creado correctamente!')
                return redirect('/home')
            except:
                messages.error(request,'Error al crear el usuario padre!')
                pass
    else:
        form = PadreUserForm()
    return render(request,'School/padre-user.html',{'form':form,'parents':parents})



@login_required(login_url="/login")
@staff_member_required
def add_subjects(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"Asignatura creada correctamente!")
                return redirect('/add-subjects')
            except:
                messages.error(request,'Error al crear una asignatura!')
                pass
    else:
        form = SubjectForm()
    return render(request,'School/add-library.html',{'form': form,'courses': courses})

@login_required(login_url="/login")
@staff_member_required
def add_periodo(request):
    periodos = Periodo.objects.all()
    if request.method == 'POST':
        form = PeriodoForm(request.POST)
        
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"Periodo creado correctamente!")
                return redirect('/add-periodo')
            except:
                messages.error(request,'Error al crear una asignatura!')
                pass
    else:
        form = PeriodoForm()
    return render(request,'School/periodo.html',{'form': form,'periodos': periodos})

@login_required(login_url="/login")
@staff_member_required
def do_inscription(request):
    students = Students.objects.all()
    courses = Course.objects.all()
    inscriptions = Inscription.objects.all()
    periodo =  Periodo.objects.all()
    if request.method == 'POST':
        print(request.POST)
        form = InscriptionForm(request.POST)


        dat = request.POST.get('end_date').replace(",","")
        final_date = datetime.strptime(dat.replace(" ","-"), '%d-%b-%Y').date()
        start = request.POST.get('start_date').replace(",","")
        begin_date = datetime.strptime(start.replace(' ','-'), '%d-%b-%Y').date()
        inscripcion = Inscription.objects.filter(student_id_id=request.POST.get('student_id'),start_date__gte=datetime.strftime(begin_date,'%Y-%m-%d'),end_date__lte=datetime.strftime(final_date, '%Y-%m-%d'))
        
        if inscripcion.count()>0:
            print("No se puede inscribir el mismo estudiante en la misma fecha sin finalizar el periodo escolar")
            messages.error(request,'Error, estudiante ya inscrito!')
        else:
            if periodo[0].final < timezone.now():
                print("Periodo de inscripcion finalizado!")
                messages.error(request,'Periodo de inscripcion finalizado!')
            else:
                print("Inscrito!")
                #messages.success(request,'Inscrito!')
                #form = InscriptionForm()
                #print(request.POST)
                if form.is_valid():
                    try:
                        form.save()
                        messages.success(request,'Inscripcion procesada!')
                        return redirect('/do-inscription')
                    except:
                        messages.error(request,'Error al procesar la inscripcion!')
                        pass
    else:
        form = InscriptionForm()
    
    return render(request,'School/add-fees.html',{'form':form,'students':students,'courses':courses,'inscriptions':inscriptions,'periodo':periodo})

@login_required(login_url="/login")
@staff_member_required
def add_students(request):
    students = Students.objects.all()
    if request.method == 'POST':
            val_student = Students.objects.filter(id_number=request.POST.get('id_number'))
            
            if val_student.count()>0:
                print("La matricula existe!")
                messages.error(request,'Error, la matricula ya existe!')   
                form = StudentForm
            else:
                if len(request.POST.get('id_number')) > 8 or len(request.POST.get('id_number')) < 8:
                    print("La matricula debe ser de 8 digitos")
                    messages.error(request,'La matricula debe ser de 8 digitos!')
                    form = StudentForm()
                else:
                    form = StudentForm(request.POST)
                    if form.is_valid():
                        try:
                            form.save()
                            messages.success(request,'Estudiante creado correctamente!')
                            return redirect('/add-students')
                        except:
                            messages.error(request,'Error al crear un estudiante!')
                            pass
    else:
        form = StudentForm
    return render(request,'School/add-student.html',{'form': form,'students':students})

@login_required(login_url="/login")
@staff_member_required
def add_staff(request):
    data = {
        'form': CustomUserCreationForm()
    }
    print(request.POST)
    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                messages.success(request,'Usuario creado correctamente!')
                UnassignedUser.objects.create(user=user)
                return redirect('/add-staff')
            except:
                pass
        data["form"] = form



    return render(request,'School/add-staff.html',data)


@login_required(login_url="/login")
@staff_member_required
def add_professor(request):
    teachers = Teachers.objects.all()
    if request.method == 'POST':
        
            
            val_teacher = Teachers.objects.filter(Q(code=request.POST.get('code')) | Q(id_number=request.POST.get('id_number')))
            print(val_teacher.count())
            if val_teacher.count() > 0:
                print("La matricula o cedula ya existe")
                messages.success(request,'La matricula o la cedula ya existe!')
                form = TeacherForm()
            else:
                if len(request.POST.get('code')) > 8 or len(request.POST.get('id_number')) > 11 or len(request.POST.get('code')) < 8 or len(request.POST.get('id_number')) < 11:
                    print("Revise la cedula o la matricula, recuerde que la cedula debe ser de 11 y la matricula de 8 digitos")
                    messages.success(request,'Revise la cedula o matricula, recordando que la cedula debe ser de 11 digitos y la matricula de 8 digitos!')
                    form = TeacherForm()
                else:
                    form = TeacherForm(request.POST)
                    if form.is_valid():
                        try:
                            form.save()
                            messages.success(request,'Profesor creado correctamente!')
                            return redirect('/add-professor')
                        except:
                            messages.error(request,'Error al crear el profesor!')
                            pass
    else:
        form = TeacherForm
    return render(request,'School/add-professor.html',{'form': form,'teachers':teachers})

@login_required(login_url="/login")
@staff_member_required
def add_parents(request):
    if request.method == 'POST':
        val_parent = Parents.objects.filter(Q(id_number=request.POST.get('id_number')))
        if val_parent.count() > 0:
            print("La cedula ya existe")
            messages.error(request,'La cedula ya existe!')
            form = ParentForm()
        else:
            cedula = request.POST.get('id_number')
            if len(cedula)> 11 or len(cedula) < 11:
                print("La cedula tiene que ser de 11 digitos!")
                messages.error(request,'La cedula debe ser de 11 digitos')
                form = ParentForm()
            else:
                form = ParentForm(request.POST)
                if form.is_valid():
                    try:
                        form.save()
                        messages.success(request,'Padre creado correctamente!')
                        return redirect('/add-parents')
                    except:
                        messages.error(request,'Error al crear padre!')
                        pass
    else:
        form = ParentForm
    return render(request,'School/add-departments.html',{'form': form})

@login_required(login_url="/login")
@staff_member_required
def edit_student(request):
    students = Students.objects.all()
    template = "School/edit-student.html"
    return render(request,template,{'students':students})

@login_required(login_url="/login")
@staff_member_required
def edit_periodo(request):
    periodos = Periodo.objects.all()
    template = "School/edit-periodo.html"
    return render(request,template,{'periodos':periodos})

@login_required(login_url="/login")
@staff_member_required
def edit_mensualidad(request):
    cobros = Cobro.objects.all()
    template = "School/edit-tarifa.html"
    return render(request,template,{'cobros':cobros})


@login_required(login_url="/login")
@staff_member_required
def edit_inscription(request):
    inscription = Inscription.objects.all()
    courses = Course.objects.all()
    students = Students.objects.all()
    template = "School/edit-inscriptions.html"
    return render(request,template,{'inscription':inscription,'students':students,'courses':courses})

@login_required(login_url='/login')
@staff_member_required
def edit_staff(request):
    usernames = User.objects.all()
    template = "School/edit-staff.html"
    return render(request,template,{'usernames':usernames})


@login_required(login_url="/login")
@staff_member_required
def edit_professor(request):
    teachers = Teachers.objects.all()
    template = "School/edit-professor.html"
    return render(request,template,{'teachers':teachers})

@login_required(login_url="/login")
@staff_member_required
def edit_parents(request):
    parents = Parents.objects.all()
    template = "School/edit-departments.html"
    return render(request,template,{'parents':parents})

@login_required(login_url="/login")
@staff_member_required
def edit_subjects(request):
    subjects = Subject.objects.all()
    courses = Course.objects.all()
    template = "School/edit-library.html"
    return render(request,template,{'subjects':subjects,'courses':courses})

@login_required(login_url="/login")
@staff_member_required
def edit_courses(request):
    courses = Course.objects.all()
    template = "School/edit-courses.html"
    return render(request,template,{'courses':courses})

@login_required(login_url="/login")
@staff_member_required
def edit_st(request,id):
    students_v = Students.objects.get(id=id)
    students = Students.objects.all()
    template = "School/edit-student.html"
    return render(request,template,{'students':students,'students_v':students_v})

@login_required(login_url="/login")
@staff_member_required
def edit_periodo_b(request,id):
    periodos_v = Periodo.objects.get(id=id)
    periodos = Periodo.objects.all()
    template = "School/edit-periodo.html"
    return render(request,template,{'periodos':periodos,'periodos_v':periodos_v})

@login_required(login_url="/login")
@staff_member_required
def edit_inscription_b(request,id):
    inscription_v = Inscription.objects.get(id=id)
    inscription = Inscription.objects.all()
    courses =  Course.objects.all()
    students = Students.objects.all()
    template = "School/edit-inscriptions.html"
    return render(request,template,{'inscription':inscription,'inscription_v':inscription_v,'students':students,'courses':courses})


@login_required(login_url="/login")
@staff_member_required
def edit_professor_b(request,id):
    teachers_v = Teachers.objects.get(id=id)
    teachers = Teachers.objects.all()
    template = "School/edit-professor.html"
    return render(request,template,{'teachers':teachers,'teachers_v':teachers_v})

@login_required(login_url="/login")
@staff_member_required
def edit_mensualidad_b(request,id):
    cobros_v = Cobro.objects.get(id=id)
    cobros = Cobro.objects.all()
    template = "School/edit-tarifa.html"
    return render(request,template,{'cobros':cobros,'cobros_v':cobros_v})



@login_required(login_url="/login")
@staff_member_required
def edit_staff_b(request,id):
    usernames_v = User.objects.get(id=id)
    usernames = User.objects.all()
    template = "School/edit-staff.html"
    return render(request,template,{'usernames':usernames,'usernames_v':usernames_v})

@login_required(login_url="/login")
@staff_member_required
def edit_parents_b(request,id):
    parents_v = Parents.objects.get(id=id)
    parents = Parents.objects.all()
    template = "School/edit-departments.html"
    return render(request,template,{'parents':parents,'parents_v':parents_v})

@login_required(login_url="/login")
def edit_subjects_b(request,id):
    subjects_v = Subject.objects.get(id=id)
    subjects = Subject.objects.all()
    courses = Course.objects.all()
    template = "School/edit-library.html"
    return render(request,template,{'subjects':subjects,'subjects_v':subjects_v,'courses':courses})

@login_required(login_url="/login")
@staff_member_required
def edit_courses_b(request,id):
    courses_v = Course.objects.get(id=id)
    courses = Course.objects.all()
    template = "School/edit-courses.html"
    return render(request,template,{'courses':courses,'courses_v':courses_v})

@login_required(login_url="/login")
@staff_member_required
def edit_courses_confirm(request,id):
    courses_v = Course.objects.get(id=id)
    courses = Course.objects.all()
    template = "School/edit-courses.html"
    form = CourseForm(request.POST, instance=courses_v)
    if form.is_valid():
        try:
            form.save()
            messages.success(request,'Curso modificado correctamente!')
            return redirect('/edit-courses')
        except:
            messages.error(request,'Error al modificar curso!')
            pass
    return render(request,template,{'courses':courses,'courses_v':courses_v})

@login_required(login_url="/login")
@staff_member_required
def edit_periodo_confirm(request,id):
    periodos_v = Periodo.objects.get(id=id)
    periodos = Periodo.objects.all()
    template = "School/edit-periodo.html"
    form = PeriodoForm(request.POST, instance=periodos_v)
    if form.is_valid():
        try:
            form.save()
            messages.success(request,'Periodo modificado correctamente!')
            return redirect('/edit-periodo')
        except:
            messages.error(request,'Error al modificar periodo!')
            pass
    return render(request,template,{'periodos':periodos,'periodos_v':periodos_v})

@login_required(login_url="/login")
@staff_member_required
def edit_mensualidad_confirm(request,id):
    cobros_v = Cobro.objects.get(id=id)
    cobros = Cobro.objects.all()
    template = "School/edit-courses.html"
    form = CobroForm(request.POST, instance=cobros_v)
    if form.is_valid():
        try:
            form.save()
            messages.success(request,'Mensualidad modificada correctamente!')
            return redirect('/edit-mensualidad')
        except:
            messages.error(request,'Error al modificar la mensualidad!')
            pass
    return render(request,template,{'cobros':cobros,'cobros_v':cobros_v})

@login_required(login_url="/login")
@staff_member_required
def edit_inscription_confirm(request,id):
    inscription_v = Inscription.objects.get(id=id)
    inscription = Inscription.objects.all()
    courses = Course.objects.all()
    students = Students.objects.all()
    template = "School/edit-inscriptions.html"
    form = InscriptionForm(request.POST, instance=inscription_v)
    print(request.POST)
    if form.is_valid():
        try:
            form.save()
            messages.success(request,'Inscripcion modificada correctamente!')
            return redirect('/edit-inscription')
        except:
            messages.error(request,'Error al modificar la inscripcion!')
            pass
    return render(request,template,{'inscription':inscription,'inscription_v':inscription_v,'courses':courses,'students':students})


@login_required(login_url="/login")
@staff_member_required
def edit_subjects_confirm(request,id):
    subjects_v = Subject.objects.get(id=id)
    subjects = Subject.objects.all()
    template = "School/edit-library.html"
    form = SubjectForm(request.POST, instance=subjects_v)
    if form.is_valid():
        try:
            form.save()
            messages.success(request,'Asignatura modificada correctamente!')
            return redirect('/edit-subjects')
        except:
            messages.error(request,'Error al modificar la asignatura!')
            pass
    return render(request,template,{'subjects':subjects,'subjects_v':subjects_v})

@login_required(login_url="/login")
@staff_member_required
def edit_st_confirm(request,id):
    students_v = Students.objects.get(id=id)
    students = Students.objects.all()
    template = "School/edit-student.html"
    form = StudentForm(request.POST,instance=students_v)
    print(request.POST)
    if form.is_valid():
            val_student = Students.objects.filter(id_number=request.POST.get('id_number'))
            
            if val_student.count()>0:
                print("La matricula existe!")
                messages.error(request,'La matricula ya existe!')   
                form = StudentForm
            else:
                if len(request.POST.get('id_number')) > 8 or len(request.POST.get('id_number')) < 8:
                    print("La matricula debe ser de 8 digitos")
                    messages.error(request,'La matricula debe ser de 8 digitos!')
                    form = StudentForm()
                else:
                    try:
                        form.save()
                        messages.success(request,'Estudiante modificado correctamente!')
                        return redirect('/edit-student')
                    except:
                        messages.error(request,'Error al modificar un estudiante!')
                        pass
    return render(request,template,{'students':students,'students_v':students_v})

@login_required(login_url="/login")
@staff_member_required
def edit_professor_confirm(request,id):
    teachers_v = Teachers.objects.get(id=id)
    teachers = Teachers.objects.all()
    template = "School/edit-professor.html"
    form = TeacherForm(request.POST,instance=teachers_v)
    print(request.POST)
    if form.is_valid():
            val_teacher = Teachers.objects.filter(Q(code=request.POST.get('code')) | Q(id_number=request.POST.get('id_number')))
            print(val_teacher.count())
            if val_teacher.count() > 0:
                print("La matricula o cedula ya existe")
                messages.error(request,'La matricula o la cedula ya existe!')
                form = TeacherForm()
            else:
                if len(request.POST.get('code')) > 8 or len(request.POST.get('id_number')) > 11 or len(request.POST.get('code')) < 8 or len(request.POST.get('id_number')) < 11:
                    print("Revise la cedula o la matricula, recuerde que la cedula debe ser de 11 y la matricula de 8 digitos")
                    messages.error(request,'Verifique la cedula o la matricula, recordando que la cedula debe ser de 11 digitos y la matricula de 8 digitos!')
                    form = TeacherForm()
                else:
                    try:
                        form.save()
                        messages.success(request,'Profesor modificado correctamente!')
                        return redirect('/edit-professor')
                    except:
                        messages.error(request,'Error al modificar un profesor!')
                        pass
    return render(request,template,{'teachers':teachers,'teachers_v':teachers_v})

@login_required(login_url="/login")
@staff_member_required
def edit_staff_confirm(request,id):
    
    usernames_v = User.objects.get(id=id)
    usernames = User.objects.all()
    template = "School/edit-staff.html"
    data = {
        'form': CustomUserCreationForm()
    }
    form = CustomUserCreationForm(data=request.POST,instance=usernames_v)
    print(request.POST)
    if form.is_valid():
        try:

            form.save()
            messages.success(request,'Usuario modificado correctamente!')
            return redirect('/edit-staff')
        except:
            messages.error(request,'Error al modificar un usuario!')
            pass
    return render(request,template,{'usernames':usernames,'usernames_v':usernames_v})
    
    
@login_required(login_url="/login")
@staff_member_required
def edit_parents_confirm(request,id):
    parents_v = Parents.objects.get(id=id)
    parents = Parents.objects.all()
    template = "School/edit-departments.html"
    form = ParentForm(request.POST,instance=parents_v)
    print(request.POST)
    if form.is_valid():
        val_parent = Parents.objects.filter(Q(id_number=request.POST.get('id_number')))
        if val_parent.count() > 0:
            print("La cedula ya existe")
            messages.error(request,'La cedula ya existe!')
            form = ParentForm()
        else:
            cedula = request.POST.get('id_number')
            if len(cedula)> 11 or len(cedula) < 11:
                print("La cedula tiene que ser de 11 digitos!")
                messages.error(request,'La cedula debe ser de 11 digitos!')
                form = ParentForm()
            else:
                form.save()
                return redirect('/edit-parents')
    return render(request,template,{'parents':parents,'parents_v':parents_v})

@login_required(login_url="/login")
@staff_member_required
def search_course(request):
    template = "School/edit-courses.html"

    if request.method == "GET":
        s_courses = Course.objects.filter(level__icontains=request.GET)
        if s_courses.exists():
            return render(request,template,{'s_courses':s_courses})
    
class SearchResultsView(LoginRequiredMixin,ListView):
    model = Course
    login_url = '/login'
    template_name = 'School/edit-courses.html'
    @staff_member_required
    def get_queryset(self): # new
        query = self.request.GET.get("search")
        s_courses = Course.objects.filter(level__icontains = query)
        print(s_courses[0].level)
        return s_courses

class SearchSubjectView(LoginRequiredMixin,ListView):
    model: Subject
    login_url = '/login'
    template_name = 'School/edit-library.html'
    @staff_member_required
    def get_queryset(self):
        query = self.request.GET.get("search")
        s_subjects = Subject.objects.filter(Q(name__icontains = query) | Q(description__icontains = query) | Q(level__icontains=query))
        return s_subjects

class SearchStudentView(LoginRequiredMixin,ListView):
    model: Students
    login_url = '/login'
    template_name = 'School/edit-student.html'
    @staff_member_required
    def get_queryset(self):
        query = self.request.GET.get("search")
        s_student = Students.objects.filter(Q(first_name__icontains = query) | Q(last_name__icontains = query) | Q(id_number__icontains=query) | Q(mail__icontains = query) | Q(phone_number__icontains = query))
        return s_student

class SearchParentView(LoginRequiredMixin,ListView):
    model: Parents
    login_url = '/login'
    template_name = 'School/edit-departments.html'
    @staff_member_required
    def get_queryset(self):
        query = self.request.GET.get("search")
        s_parent = Parents.objects.filter(Q(first_name__icontains = query) | Q(last_name__icontains = query) | Q(id_number__icontains=query) | Q(mail__icontains = query) | Q(phone_number__icontains = query))
        return s_parent

class SearchUserView(LoginRequiredMixin,ListView):
    model: User
    login_url = '/login'
    template_name = 'School/edit-staff.html'
    @staff_member_required
    def get_queryset(self):
        query = self.request.GET.get("search")
        s_staff = User.objects.filter(Q(username__icontains = query) | Q(email__icontains = query) | Q(first_name__icontains = query) | Q(last_name__icontains = query))
        return s_staff

class SearchTeacherView(LoginRequiredMixin,ListView):
    model: Teachers
    login_url = '/login'
    template_name = 'School/edit-professor.html'
    @staff_member_required
    def get_queryset(self):
        query = self.request.GET.get("search")
        s_teacher = Teachers.objects.filter(Q(first_name__icontains = query) | Q(last_name__icontains = query) | Q(code__icontains = query) | Q(id_number__icontains=query) | Q(mail__icontains = query) | Q(phone_number__icontains = query))
        return s_teacher

class SearchSelectProfessorView(LoginRequiredMixin,ListView):
    model: Teachers
    login_url = '/login'
    template_name = 'School/select_teacher.html'
    @staff_member_required
    def get_queryset(self):
        query = self.request.GET.get("search")
        s_teacher = Teachers.objects.filter(Q(first_name__icontains = query) | Q(last_name__icontains = query) | Q(code__icontains = query) | Q(id_number__icontains=query) | Q(mail__icontains = query) | Q(phone_number__icontains = query))
        return s_teacher

class SearchSelectStudentView(LoginRequiredMixin,ListView):
    model: Students
    login_url = '/login'
    template_name = 'School/select_student.html'
    @staff_member_required
    def get_queryset(self):
        query = self.request.GET.get("search")
        s_student = Students.objects.filter(Q(first_name__icontains = query) | Q(last_name__icontains = query) | Q(id_number__icontains=query) | Q(mail__icontains = query) | Q(phone_number__icontains = query))
        return s_student