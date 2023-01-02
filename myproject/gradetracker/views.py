from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'templates/layouts/home.html') 


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Log the user in
            return render(request, 'layouts/index.html', {'students': students, 'teachers': teachers, 'courses': courses}) # redirect to the 'index' view function
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        context = {"form": register_form}
        if register_form.is_valid():
            # process the form data (e.g., create a new user)
            return redirect('login')
    else:
        register_form = RegisterForm()
    return render(request, 'users/register.html',context)

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
        context= {"form":form}
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'gradetracker/add_student.html',context)

def students(request):
    students = Student.objects.all()
    return render(request, 'templates/students/students.html', {'students': students})

def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def home(request):
    return render(request, 'layouts/home.html')

def index(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    courses = Course.objects.all()
    return render(request, 'index.html', {'students': students, 'teachers': teachers, 'courses': courses})