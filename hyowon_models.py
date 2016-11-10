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
        return self.student + attendance + str(self.date)

    
    # 아래 내용은 작동 확인을 못했습니다 ㅠㅠ 테스트를 못한 코드라 아마도 오류가 있을듯 합니다..

    # 출석체크를 시작할 때

    def check_start(cls):
        student_list = Student.objects.all()
        for student in student_list:
            Attendance.objects.create(student=student)
            
    # 출석을 처리할 때

    def attend(self):
        Attendance.objects.filter(student=self.student, date=date.today())[0].checked = True
