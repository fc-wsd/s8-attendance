from django.db import models
from datetime import date

class Student(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    student = models.ForeignKey(Student)
    checked = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
