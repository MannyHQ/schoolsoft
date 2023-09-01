from django.urls import path
from . import views

app_name = "teachers"
urlpatterns = [
    path("teachers/", views.teachers, name="teachers"),
    path("courses/", views.lista_curso, name="courses"),
    path('calificar/', views.calificar, name='calificar'),
    path('calification/', views.califications, name='calification'),
]