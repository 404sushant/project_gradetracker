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

]