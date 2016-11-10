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
        if self.checked:
            attendance = "출석"
        else:
            attendance = "결석"
        return self.student.name + ", " + attendance + ", " + str(self.date)


    # 출석체크를 시작할 때: 등록된 학생 모두를 불러옴

    def check_start():
        student_list = Student.objects.all()
        for student in student_list:
            Attendance.objects.get_or_create(student=student, date=date.today())

    # 출석을 처리할 때

    def attend(self):
        self.checked = True
        self.save()
