from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def home(request):
    return render(request, 'templates/layouts/home.html') 


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Log the user in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                # redirect to the appropriate view based on the user type
                if user.is_superuser:
                    return redirect('add_student')
                elif user.is_teacher:
                    return redirect('teachers')
                else:
                    return redirect('students')
            else:
                # Return an 'invalid login' error message.
                return render(request, 'users/login.html', {'form': form, 'error_message': 'Invalid login'})
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})



@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # process the form data (e.g., create a new user)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']

            # create the user based on the user type
            if user_type == 'student':
                # create a new student
                student = Student.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
                student.save()
            elif user_type == 'teacher':
                # create a new teacher
                teacher = Teacher.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
                teacher.save()
            else:
                # create a new administrator
                administrator = Administrator.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
                administrator.save()

            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def is_admin(user):
    return user.is_staff
def add_student(request):
    context = {"form": None}
    if request.user.is_authenticated and request.user.is_admin:  # check if user is authenticated and an administrator
        if request.method == 'POST': 
            form = AddStudentForm(request.POST)
            context["form"] = form
            if form.is_valid():
                form.save()
                return redirect('students')
        else:
            context= {"form":form}
        return render(request, 'administrator/add_student.html',context)
    else:
        # user is not authenticated or not an administrator
        return render(request, '403.html', {}, status=403)  # return a 403 Forbidden error


@login_required
@user_passes_test(is_admin)
def edit_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        form = AddStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = AddStudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect('students')


def students(request):
    students = Student.objects.all()
    return render(request, 'templates/students/students.html', {'students': students})

def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def edit_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/edit_course.html', {'form': form, 'course': course})


def home(request):
    return render(request, 'layouts/home.html')

def index(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    courses = Course.objects.all()
    return render(request, 'index.html', {'students': students, 'teachers': teachers, 'courses': courses})
@login_required
def add_student(request):
    context = {"form": None}
    if request.user.is_authenticated and request.user.is_superuser:  # check if user is authenticated and an administrator
        if request.method == 'POST': 
            form = AddStudentForm(request.POST)
            context["form"] = form
            if form.is_valid():
                form.save()
                return redirect('students')
        else:
            form = AddStudentForm()
            context= {"form":form}
        return render(request, 'administrator/add_student.html',context)
    else:
        # user is not authenticated or not an administrator
        return render(request, '403.html', {}, status=403)  # return a 403 Forbidden error

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Log the user in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                # redirect to the appropriate view based on the user type
                if user.is_admin:
                    return redirect('add_student')
                elif user.is_teacher:
                    return redirect('teachers')
                else:
                    return redirect('students')
            else:
                # Return an 'invalid login' error message.
                return render(request, 'users/login.html', {'form': form, 'error_message': 'Invalid login'})
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})
