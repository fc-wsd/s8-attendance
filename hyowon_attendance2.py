class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Attendance:
    def __init__(self):
        self.attendance_list = []

    def attend(self, student):
        if type(student) is Student:
            self.attendance_list.append(student)
        else:
            print("등록된 학생이 아닙니다.")

    def list(self):
        return [student.name for student in self.attendance_list]
