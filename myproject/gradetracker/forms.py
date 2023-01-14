from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=20, widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('administrator', 'Administrator')])
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'course',  'score']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'semester']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['course', 'name', 'due_date', 'points_possible','type']

class AdministratorForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = ['first_name', 'last_name', 'email', 'password','role']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'password','subject']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'student_id', 'password', ]

class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'student_id', 'password', ]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'credits']

class AddStudentForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=20, widget=forms.PasswordInput)
    student_id = forms.CharField(max_length=20)
    gpa = forms.DecimalField(max_digits=4, decimal_places=2)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data
