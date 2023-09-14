from django.urls import path
from . import views


app_name = 'students'
urlpatterns=[
    path('student/',views.estudiante, name='students'),
    path('qualification/',views.ver_calificaciones, name='qualification'),
    path('subjects/',views.ver_asignaturas, name='subjects'),
    path('info/',views.informacion, name='subjects'),
    path('generate_pdf/',views.getpdf,name='generar_pdf'),
]