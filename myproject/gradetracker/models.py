from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    credits = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    student_id = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.student_id})'

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.subject})'

class Administrator(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.role})'

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    due_date = models.DateField()
    points_possible = models.PositiveIntegerField()
    type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} ({self.type}) - {self.course}'

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.student} - {self.course} ({self.status})'

class Grade(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.student} - {self.course}: {self.score}'
