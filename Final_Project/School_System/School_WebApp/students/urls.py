from django.urls import path
from . import views


app_name = 'students'
urlpatterns=[
    path('student/',views.lista_asignatura, name='students'),
    path('student-calification/',views.notes_list, name='calification'),
    path('student-subject/',views.subject_list, name='subject'),
]