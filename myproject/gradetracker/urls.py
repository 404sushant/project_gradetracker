from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
        path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('students/',views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('courses/', views.courses, name='courses'),
    path('edit-course/<int:course_id>/', views.edit_course, name='edit_course'),

    path('add-student/', views.add_student, name='add_student'),
    path('edit-student/<int:student_id>/', views.edit_student, name='edit_student'),


]