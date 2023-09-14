from dataclasses import fields
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
            'id_number': forms.NumberInput(attrs={'class': 'form-control','maxlength':'11'}),
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CobroForm(forms.ModelForm):
    class Meta:
        model = Cobro
        fields = ['mensualidad']
        widgets = {
            'mensualidad': forms.NumberInput(attrs={'class':'form-control'}),
        }

class UserManagementForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password','password1','password2','is_superuser','is_staff','is_active']
        widgets ={
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name','is_staff','is_active']
        widgets ={
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
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


class PadreUserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['id_usuario','nombre_user','password','correo','estado']
        widgets = {
            'id_usuario': forms.Select(attrs={'class': 'form-control'}),
            'nombre_user': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }
class PeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ['inicio','final','inicio_escolar','fin_escolar']
        widgets = {
            'inicio': forms.TextInput(attrs={'class': 'datepicker-default form-control'}),
            'final': forms.TextInput(attrs={'class': 'datepicker-default form-control'}),
            'inicio_escolar': forms.TextInput(attrs={'class': 'datepicker-default form-control'}),
            'fin_escolar': forms.TextInput(attrs={'class': 'datepicker-default form-control'}),
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
            'id_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ['first_name','last_name','code','mail','phone_number','id_number','status']
        widgets ={
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.NumberInput(attrs={'class': 'form-control'}),
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class TeacherSubjectForm(forms.ModelForm):
    asginaturas = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'select2'}))
    class Meta:
        model = Teacher_VS_Subjects
        fields = ['subject_id']



class AssignUserForm(forms.Form):
    identification = forms.CharField(max_length=11, label="Matrícula o Cédula")
    
    class Meta:
        widgets ={
            'identification': forms.TextInput(attrs={'name': 'identification'}),
        }
    
    def clean_identification(self):
        identification = self.cleaned_data['identification']
        # Agrega la lógica necesaria para validar la matrícula o cédula según corresponda
        return identification



class RemoveSubjectForm(forms.Form):
    asignaturas = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'select2'}))

    def __init__(self, profesor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        asignaturas_asignadas = profesor.teacher_vs_subjects_set.all()
        self.fields['asignaturas'].queryset = asignaturas_asignadas
