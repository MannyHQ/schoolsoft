from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parents
        fields = ['first_name','last_name','id_number','mail','phone_number','status']
        widgets ={
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UserManagementForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']
        widgets ={
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
    

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['level']
        widgets = {
            'level': forms.TextInput(attrs={'class': 'form-control'})
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name','start_date','description','level']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.TextInput(attrs={'class': 'datepicker-default form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
        }

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = ['date_inscription','start_date','end_date','course_id','student_id','inscription_status']
        widgets = {
            'date_inscription': forms.TextInput(attrs={'class': 'datepicker-default form-control'}),
            'start_date': forms.TextInput(attrs={'class': 'datepicker-default form-control'}),
            'end_date': forms.TextInput(attrs={'class': 'datepicker-default form-control'}),
            'inscription_status': forms.TextInput(attrs={'class': 'form-control'}),
            'course_id': forms.Select(attrs={'class': 'form-control'}),
            'student_id': forms.Select(attrs={'class': 'form-control'}),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['first_name','last_name','birthdate','gender','id_number','mail','phone_number','status']
        widgets ={
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birthdate': forms.TextInput(attrs={'class': 'datepicker-default form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ['first_name','last_name','code','mail','phone_number','id_number','status']
        widgets ={
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class TeacherSubjectForm(forms.ModelForm):
    asginaturas = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'select2'}))
    class Meta:
        model = Teacher_VS_Subjects
        fields = ['subject_id']

class RemoveSubjectForm(forms.Form):
    asignaturas = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'select2'}))

    def __init__(self, profesor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        asignaturas_asignadas = profesor.teacher_vs_subjects_set.all()
        self.fields['asignaturas'].queryset = asignaturas_asignadas