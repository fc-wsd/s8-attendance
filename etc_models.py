# • Django 프로젝트를 생성한 후 Django 앱을 만드세요.
# • 학생 정보를 다루는 `Student` 모델과 출석 정보를 다루는 `Attendance` 모델을 만드세요.#
# • 모델 파일만 제출하세요.

from django.db import models


# Create your models here.
class Student(models.Model):
    no = models.CharField(max_length=8, primary_key=True, auto_created=False)   # 학번
    name = models.CharField(max_length=4, db_index=True, null=False)            # 이름
    grade = models.PositiveSmallIntegerField(null=False)                        # 학년
    num_class = models.PositiveSmallIntegerField(null=False)                    # 반

    def __str__(self):
        return '{}'.format(self.no)


class Attendance(models.Model):
    no = models.ForeignKey(Student)
    a_date = models.DateField(auto_now_add=True)
