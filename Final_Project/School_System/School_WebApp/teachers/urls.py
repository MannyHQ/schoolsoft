from django.urls import path
from . import views


urlpatterns = [
    path("teachers/", views.teachers, name="teachers"),
    path("notes/", views.notes_teacher, name="notes_teacher"),
    path("courses/", views.lista_curso, name="courses"),
    path('calificar/', views.calificar, name='calificar'),
    path('calification/', views.califications, name='calification'),
    path('courses_califications/', views.teacher_course_califications, name='course_califications'),
]