from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'templates/layouts/home.html') 


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Log the user in
            return redirect('home')
    return render(request, 'gradetracker/templates/users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # process the form data (e.g., create a new user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_report')
    else:
        form = GradeForm()
    return render(request, 'gradetracker/add_grade.html',
    {
        'form': form
        }
    )

def add_student(request):
    if request.method == 'POST': 
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'gradetracker/add_student.html',
    {
        'form': form,
        }
    )
