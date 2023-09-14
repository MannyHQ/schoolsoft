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
    path("", include('students.urls')),
    path("", include('teachers.urls')),
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
    path('',views.login_us,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('edit-staff/',views.edit_staff,name="edit-staff"),
    path('edit-staff/<int:id>',views.edit_staff_b,name="edit-staff"),
    path('edit-staff/update/<int:id>',views.edit_staff_confirm,name="update"),
    path('search-courses/',views.SearchResultsView.as_view(),name="search-courses"),
    path('search-subjects/',views.SearchSubjectView.as_view(),name="search-subjects"),
    path('search-students/',views.SearchStudentView.as_view(), name = "search-students"),
    path('search-parents/',views.SearchParentView.as_view(), name = "search-parents"),
    path('search-staff/',views.SearchUserView.as_view(), name = "search-staff"),
    path('search-teachers/',views.SearchTeacherView.as_view(), name = "search-teachers"),
    path('search-selteachers/',views.SearchSelectProfessorView.as_view(), name = "search-selteachers"),
    path('search-selstudent/',views.SearchSelectStudentView.as_view(), name = "search-selstudent"),
    path('all-students/',views.all_students,name='all-students'),
    path('user-student/',views.assign_student_user,name='user-student'),
    path('user-teacher/',views.assign_teacher_user,name='user-teacher'),
    path('user-parent/',views.assign_parent_user,name='user-parent'),
    path('all-courses/', views.all_courses, name='all-course'),
    path('all-subjects/',views.all_subjects,name='all-subjects'),
    path('all-parents/',views.all_parents,name='all-parents'),
    path('all-staff/',views.all_staff,name='all-staff'),
    path('all-inscription/',views.all_inscription,name='all-inscription'),
    path('edit-inscription/',views.edit_inscription,name='edit-inscription'),
    path('edit-inscription/<int:id>',views.edit_inscription_b,name='edit-inscription'),
    path('edit-inscription/update/<int:id>',views.edit_inscription_confirm,name='update'),
    path('parent-user/',views.crear_usuario_padre,name='parent-user/'),
    path('bills/',views.lista_pagos, name='bills'),
    path('mensualidad/',views.add_mensualidad,name='mensualidad'),
    path('edit-mensualidad/',views.edit_mensualidad,name='edit-mensualidad'),
    path('edit-mensualidad/<int:id>',views.edit_mensualidad_b,name='edit-mensualidad'),
    path('edit-mensualidad/update/<int:id>',views.edit_mensualidad_confirm,name='update'),
    path('add-periodo/',views.add_periodo,name='periodo'),
    path('edit-periodo/',views.edit_periodo,name='edit-periodo'),
    path('edit-periodo/<int:id>',views.edit_periodo_b,name='edit-periodo'),
    path('edit-periodo/update/<int:id>',views.edit_periodo_confirm,name='update')
    
]

urlpatterns += [
    path('', RedirectView.as_view(url='School/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)