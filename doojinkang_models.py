from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=40)

class Attendance(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    Student = models.ForeignKey(Student)

