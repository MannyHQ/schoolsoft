from django.shortcuts import get_object_or_404,render,redirect
from .models import Students,Teachers,Parents,Subject,Course,Inscription
from django.http import HttpResponse
from django.template import loader
from School.forms import *
from School.models import *
def index(request):
    students_count = Students.objects.count()
    latest_inscriptions_list = Inscription.objects.order_by("-date_inscription")[:5]
    template = loader.get_template("school/index.html")
    context = {
        "latest_inscriptions_list": latest_inscriptions_list,
        "students_count": students_count
        
    }
    
    return HttpResponse(template.render(context,request))

def all_professors(request):
    return render(request,'School/all-professors.html')


def asignar_asignaturas(request, profesor_id):
    if request.method == 'POST':
        form = TeacherSubjectForm(request.POST)
        if form.is_valid():
            profesor = Teachers.objects.get(pk=profesor_id)
            for asignatura in form.cleaned_data['asginaturas']:
                Teacher_VS_Subjects.objects.create(teacher_id=profesor, subject_id=asignatura)
            return redirect('/home')
    else:
        form = TeacherSubjectForm()
    return render(request, 'School/assign_subject.html', {'form': form})


def quitar_asignaturas(request, profesor_id):
    profesor = get_object_or_404(Teachers, pk=profesor_id)

    if request.method == 'POST':
        asignatura_id = request.POST.get('asignatura_id')
        asignatura = get_object_or_404(Subject, pk=asignatura_id)
        Teacher_VS_Subjects.objects.filter(subject_id=asignatura, teacher_id=profesor).delete()
        return redirect('/remove-subject/{profesor_id}')

    asignaturas_asignadas = profesor.teacher_vs_subjects_set.all()
    return render(request, 'School/template.html', {'profesor': profesor, 'asignaturas_asignadas': asignaturas_asignadas})

def desasignar_asignaturas(request, profesor_id):
    profesor = get_object_or_404(Teachers, pk=profesor_id)
    asignaturas_asignadas = profesor.teacher_vs_subjects_set.all()

    if request.method == 'POST':
        asignaturas_desasignar_ids = request.POST.getlist('asignaturas_desasignar')
        asignaturas_desasignar = Subject.objects.filter(id__in=asignaturas_desasignar_ids)
        profesor.teacher_vs_subjects_set.filter(subject_id__in=asignaturas_desasignar).delete()
        return redirect('/home')

    return render(request, 'School/desasignar_asignaturas_tabla.html', {'profesor': profesor, 'asignaturas_asignadas': asignaturas_asignadas})








def select_professor(request):
    teachers = Teachers.objects.all()
    template = "School/select_teacher.html"
    return render(request,template,{'teachers':teachers})

def add_courses(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/home')
            except:
                pass
    else:
        form = CourseForm()
    return render(request,'School/add-courses.html',{'form': form})


def add_subjects(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        
        if form.is_valid():
            try:
                form.save()
                return redirect('/add-subjects')
            except:
                pass
    else:
        form = SubjectForm()
    return render(request,'School/add-library.html',{'form': form,'courses': courses})

def add_students(request):
    students = Students.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/add-students')
            except:
                pass
    else:
        form = StudentForm
    return render(request,'School/add-student.html',{'form': form,'students':students})

def add_professor(request):
    teachers = Teachers.objects.all()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/add-professor')
            except:
                pass
    else:
        form = TeacherForm
    return render(request,'School/add-professor.html',{'form': form,'teachers':teachers})

def add_parents(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/add-parents')
            except:
                pass
    else:
        form = ParentForm
    return render(request,'School/add-departments.html',{'form': form})

def edit_student(request):
    students = Students.objects.all()
    template = "School/edit-student.html"
    return render(request,template,{'students':students})

def edit_professor(request):
    teachers = Teachers.objects.all()
    template = "School/edit-professor.html"
    return render(request,template,{'teachers':teachers})

def edit_parents(request):
    parents = Parents.objects.all()
    template = "School/edit-departments.html"
    return render(request,template,{'parents':parents})

def edit_subjects(request):
    subjects = Subject.objects.all()
    template = "School/edit-library.html"
    return render(request,template,{'subjects':subjects})


def edit_courses(request):
    courses = Course.objects.all()
    template = "School/edit-courses.html"
    return render(request,template,{'courses':courses})

def edit_st(request,id):
    students_v = Students.objects.get(id=id)
    students = Students.objects.all()
    template = "School/edit-student.html"
    return render(request,template,{'students':students,'students_v':students_v})

def edit_professor_b(request,id):
    teachers_v = Teachers.objects.get(id=id)
    teachers = Teachers.objects.all()
    template = "School/edit-professor.html"
    return render(request,template,{'teachers':teachers,'teachers_v':teachers_v})

def edit_parents_b(request,id):
    parents_v = Parents.objects.get(id=id)
    parents = Parents.objects.all()
    template = "School/edit-departments.html"
    return render(request,template,{'parents':parents,'parents_v':parents_v})

def edit_subjects_b(request,id):
    subjects_v = Subject.objects.get(id=id)
    subjects = Subject.objects.all()
    template = "School/edit-library.html"
    return render(request,template,{'subjects':subjects,'subjects_v':subjects_v})

def edit_courses_b(request,id):
    courses_v = Course.objects.get(id=id)
    courses = Course.objects.all()
    template = "School/edit-courses.html"
    return render(request,template,{'courses':courses,'courses_v':courses_v})

def edit_courses_confirm(request,id):
    courses_v = Course.objects.get(id=id)
    courses = Course.objects.all()
    template = "School/edit-courses.html"
    form = CourseForm(request.POST, instance=courses_v)
    if form.is_valid():
        form.save()
        return redirect('/edit-courses')
    return render(request,template,{'courses':courses,'courses_v':courses_v})

def edit_subjects_confirm(request,id):
    subjects_v = Subject.objects.get(id=id)
    subjects = Subject.objects.all()
    template = "School/edit-library.html"
    form = SubjectForm(request.POST, instance=subjects_v)
    if form.is_valid():
        form.save()
        return redirect('/edit-subjects')
    return render(request,template,{'subjects':subjects,'subjects_v':subjects_v})


def edit_st_confirm(request,id):
    students_v = Students.objects.get(id=id)
    students = Students.objects.all()
    template = "School/edit-student.html"
    form = StudentForm(request.POST,instance=students_v)
    print(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/edit-student')
    return render(request,template,{'students':students,'students_v':students_v})

def edit_professor_confirm(request,id):
    teachers_v = Teachers.objects.get(id=id)
    teachers = Teachers.objects.all()
    template = "School/edit-professor.html"
    form = TeacherForm(request.POST,instance=teachers_v)
    print(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/edit-professor')
    return render(request,template,{'teachers':teachers,'teachers_v':teachers_v})


def edit_parents_confirm(request,id):
    parents_v = Parents.objects.get(id=id)
    parents = Parents.objects.all()
    template = "School/edit-departments.html"
    form = ParentForm(request.POST,instance=parents_v)
    print(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/edit-parents')
    return render(request,template,{'parents':parents,'parents_v':parents_v})




