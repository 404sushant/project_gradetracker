from django.urls import path
from . import views

urlpatterns = [
    path("gradetracker/", views.home, name="home"),
    path('gradetracker/register/', views.register, name='register'),
    path('gradetracker/login/', views.login, name='login'),

]