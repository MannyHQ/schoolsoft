"""
URL configuration for School_WebApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from School import views

urlpatterns = [
    path('School/', include('School.urls')),
    path('admin/', admin.site.urls),
    path('all-professors/', views.all_professors, name='all-professors'),
    path('add-students/', views.add_students, name='add-students'),
    path('home/', views.index, name='home'),
    path('edit-student/',views.edit_student,name='edit-student'),
    path("edit-student/<int:id>",views.edit_st,name="edit-student"),
    path("edit-student/update/<int:id>",views.edit_st_confirm,name="update"),
    path('add-courses/',views.add_courses, name='add-courses'),
    path('edit-courses/', views.edit_courses, name='edit-courses'),
    path('edit-courses/<int:id>', views.edit_courses_b, name='edit-courses'),
    path('edit-courses/update/<int:id>', views.edit_courses_confirm, name='update'),
    path('add-subjects/',views.add_subjects,name='add-subjects'),
    path('edit-subjects/',views.edit_subjects,name='edit-subjects'),
    path('edit-subjects/<int:id>',views.edit_subjects_b,name='edit-subjects'),
    path('edit-subjects/update/<int:id>',views.edit_subjects_confirm,name='update'),
    path('add-parents/', views.add_parents, name='add-parents'),
    path('edit-parents/', views.edit_parents, name='edit-parents'),
    path('edit-parents/<int:id>', views.edit_parents_b, name='edit-parents'),
    path('edit-parents/update/<int:id>', views.edit_parents_confirm, name='update'),
    path('add-professor/', views.add_professor, name='add-professor'),
    path('edit-professor/', views.edit_professor, name='edit-professor'),
    path('edit-professor/<int:id>', views.edit_professor_b, name='edit-professor'),
    path('edit-professor/update/<int:id>', views.edit_professor_confirm, name='update'),
    path('assign-subject/<int:profesor_id>', views.asignar_asignaturas, name='assign-subject'),
    path('select-professor/', views.select_professor, name='select-professor'),
    path('remove-subject/<int:profesor_id>', views.desasignar_asignaturas, name='remove-subject'),
    path('quitar-asignaturas/<int:profesor_id>',views.desasignar_asignaturas,name="quitar-asignatura"),
    path('select-student/', views.select_student, name='select-student'),
    path('do-inscription/',views.do_inscription,name='do-inscription'),
    path('add-staff/',views.add_staff,name="add-staff"),
    path('login/',views.login_us,name="login"),
    path('logout/',views.logout_view,name="logout"),

]

urlpatterns += [
    path('', RedirectView.as_view(url='School/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)