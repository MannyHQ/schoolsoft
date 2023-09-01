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
from django.db.models import Q

def logout_view(request):
    logout(request)
    return redirect('/login')

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
        else:
            return render(request,template)
    return render(request,template)

@login_required(login_url="/login")
def index(request):
    students_count = Students.objects.count()
    latest_inscriptions_list = Inscription.objects.order_by("-date_inscription")[:5]
    template = loader.get_template("school/index.html")
    context = {
        "latest_inscriptions_list": latest_inscriptions_list,
        "students_count": students_count
        
    }
    
    return HttpResponse(template.render(context,request))

@login_required(login_url="/login")
def all_professors(request):
    return render(request,'School/all-professors.html')

@login_required(login_url="/login")
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

@login_required(login_url="/login")
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
def desasignar_asignaturas(request, profesor_id):
    profesor = get_object_or_404(Teachers, pk=profesor_id)
    asignaturas_asignadas = profesor.teacher_vs_subjects_set.all()

    if request.method == 'POST':
        asignaturas_desasignar_ids = request.POST.getlist('asignaturas_desasignar')
        asignaturas_desasignar = Subject.objects.filter(id__in=asignaturas_desasignar_ids)
        profesor.teacher_vs_subjects_set.filter(subject_id__in=asignaturas_desasignar).delete()
        return redirect('/home')

    return render(request, 'School/desasignar_asignaturas_tabla.html', {'profesor': profesor, 'asignaturas_asignadas': asignaturas_asignadas})







@login_required(login_url="/login")
def select_professor(request):
    teachers = Teachers.objects.all()
    template = "School/select_teacher.html"
    return render(request,template,{'teachers':teachers})

def select_student(request):
    students = Students.objects.all()
    template = "School/select_student.html"
    return render(request, template,{'students':students})

@login_required(login_url="/login")
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

@login_required(login_url="/login")
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

@login_required(login_url="/login")
def do_inscription(request):
    students = Students.objects.all()
    courses = Course.objects.all()
    inscriptions = Inscription.objects.all()

    if request.method == 'POST':
        print(request.POST)
        form = InscriptionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/do-inscription')
            except:
                pass
    else:
        form = InscriptionForm()
    
    return render(request,'School/add-fees.html',{'form':form,'students':students,'courses':courses,'inscriptions':inscriptions})

@login_required(login_url="/login")
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

@login_required(login_url="/login")
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
                form.save()
                return redirect('/add-staff')
            except:
                pass
        data["form"] = form



    return render(request,'School/add-staff.html',data)


@login_required(login_url="/login")
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

@login_required(login_url="/login")
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

@login_required(login_url="/login")
def edit_student(request):
    students = Students.objects.all()
    template = "School/edit-student.html"
    return render(request,template,{'students':students})

@login_required(login_url='/login')
def edit_staff(request):
    usernames = User.objects.all()
    template = "School/edit-staff.html"
    return render(request,template,{'usernames':usernames})


@login_required(login_url="/login")
def edit_professor(request):
    teachers = Teachers.objects.all()
    template = "School/edit-professor.html"
    return render(request,template,{'teachers':teachers})

@login_required(login_url="/login")
def edit_parents(request):
    parents = Parents.objects.all()
    template = "School/edit-departments.html"
    return render(request,template,{'parents':parents})

@login_required(login_url="/login")
def edit_subjects(request):
    subjects = Subject.objects.all()
    courses = Course.objects.all()
    template = "School/edit-library.html"
    return render(request,template,{'subjects':subjects,'courses':courses})

@login_required(login_url="/login")
def edit_courses(request):
    courses = Course.objects.all()
    template = "School/edit-courses.html"
    return render(request,template,{'courses':courses})

@login_required(login_url="/login")
def edit_st(request,id):
    students_v = Students.objects.get(id=id)
    students = Students.objects.all()
    template = "School/edit-student.html"
    return render(request,template,{'students':students,'students_v':students_v})

@login_required(login_url="/login")
def edit_professor_b(request,id):
    teachers_v = Teachers.objects.get(id=id)
    teachers = Teachers.objects.all()
    template = "School/edit-professor.html"
    return render(request,template,{'teachers':teachers,'teachers_v':teachers_v})

@login_required(login_url="/login")
def edit_staff_b(request,id):
    usernames_v = User.objects.get(id=id)
    usernames = User.objects.all()
    template = "School/edit-staff.html"
    return render(request,template,{'usernames':usernames,'usernames_v':usernames_v})

@login_required(login_url="/login")
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
def edit_courses_b(request,id):
    courses_v = Course.objects.get(id=id)
    courses = Course.objects.all()
    template = "School/edit-courses.html"
    return render(request,template,{'courses':courses,'courses_v':courses_v})

@login_required(login_url="/login")
def edit_courses_confirm(request,id):
    courses_v = Course.objects.get(id=id)
    courses = Course.objects.all()
    template = "School/edit-courses.html"
    form = CourseForm(request.POST, instance=courses_v)
    if form.is_valid():
        form.save()
        return redirect('/edit-courses')
    return render(request,template,{'courses':courses,'courses_v':courses_v})

@login_required(login_url="/login")
def edit_subjects_confirm(request,id):
    subjects_v = Subject.objects.get(id=id)
    subjects = Subject.objects.all()
    template = "School/edit-library.html"
    form = SubjectForm(request.POST, instance=subjects_v)
    if form.is_valid():
        form.save()
        return redirect('/edit-subjects')
    return render(request,template,{'subjects':subjects,'subjects_v':subjects_v})

@login_required(login_url="/login")
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

@login_required(login_url="/login")
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

@login_required(login_url="/login")
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
        form.save()
        return redirect('/edit-staff')
    return render(request,template,{'usernames':usernames,'usernames_v':usernames_v})
    
    
@login_required(login_url="/login")
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

@login_required(login_url="/login")
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
    def get_queryset(self): # new
        query = self.request.GET.get("search")
        s_courses = Course.objects.filter(level__icontains = query)
        print(s_courses[0].level)
        return s_courses

class SearchSubjectView(LoginRequiredMixin,ListView):
    model: Subject
    login_url = '/login'
    template_name = 'School/edit-library.html'
    def get_queryset(self):
        query = self.request.GET.get("search")
        s_subjects = Subject.objects.filter(Q(name__icontains = query) | Q(description__icontains = query) | Q(level__icontains=query))
        return s_subjects

class SearchStudentView(LoginRequiredMixin,ListView):
    model: Students
    login_url = '/login'
    template_name = 'School/edit-student.html'
    def get_queryset(self):
        query = self.request.GET.get("search")
        s_student = Students.objects.filter(Q(first_name__icontains = query) | Q(last_name__icontains = query) | Q(id_number__icontains=query) | Q(mail__icontains = query) | Q(phone_number__icontains = query))
        return s_student

class SearchParentView(LoginRequiredMixin,ListView):
    model: Parents
    login_url = '/login'
    template_name = 'School/edit-departments.html'
    def get_queryset(self):
        query = self.request.GET.get("search")
        s_parent = Parents.objects.filter(Q(first_name__icontains = query) | Q(last_name__icontains = query) | Q(id_number__icontains=query) | Q(mail__icontains = query) | Q(phone_number__icontains = query))
        return s_parent

class SearchUserView(LoginRequiredMixin,ListView):
    model: User
    login_url = '/login'
    template_name = 'School/edit-staff.html'
    def get_queryset(self):
        query = self.request.GET.get("search")
        s_staff = User.objects.filter(Q(username__icontains = query) | Q(email__icontains = query) | Q(first_name__icontains = query) | Q(last_name__icontains = query))
        return s_staff

class SearchTeacherView(LoginRequiredMixin,ListView):
    model: Teachers
    login_url = '/login'
    template_name = 'School/edit-professor.html'
    def get_queryset(self):
        query = self.request.GET.get("search")
        s_teacher = Teachers.objects.filter(Q(first_name__icontains = query) | Q(last_name__icontains = query) | Q(code__icontains = query) | Q(id_number__icontains=query) | Q(mail__icontains = query) | Q(phone_number__icontains = query))
        return s_teacher

class SearchSelectProfessorView(LoginRequiredMixin,ListView):
    model: Teachers
    login_url = '/login'
    template_name = 'School/select_teacher.html'
    def get_queryset(self):
        query = self.request.GET.get("search")
        s_teacher = Teachers.objects.filter(Q(first_name__icontains = query) | Q(last_name__icontains = query) | Q(code__icontains = query) | Q(id_number__icontains=query) | Q(mail__icontains = query) | Q(phone_number__icontains = query))
        return s_teacher

class SearchSelectStudentView(LoginRequiredMixin,ListView):
    model: Students
    login_url = '/login'
    template_name = 'School/select_student.html'
    def get_queryset(self):
        query = self.request.GET.get("search")
        s_student = Students.objects.filter(Q(first_name__icontains = query) | Q(last_name__icontains = query) | Q(id_number__icontains=query) | Q(mail__icontains = query) | Q(phone_number__icontains = query))
        return s_student