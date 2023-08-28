from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'School'
urlpatterns = [
    
    path("", views.index, name="index"),
    path("all-professors/", views.all_professors, name="all-professors"),
    path("add-students/",views.add_students,name='add-students'),
    path("add-student/<int:id>",views.edit_st,name="edit-student")


]




