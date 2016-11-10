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

    def __str__(self):
        if self.is_attended:
            attendance = "출석"
        else:
            attendance = "결석"
        return self.student.name + attendance + str(self.date)
