# • 학생 명단이 있는 `list`형 객체 `students` 명단.
# • 학생은 `Student` 클래스로 생성.
# • 필수 정보 : 이름
# • 출석부는 `Attendance` 클래스로 생성한 객체.
# • `attend()` 인스턴스 메서드로 출석 처리하며, 인자는 `Student` 클래스로 만든 학생 객체.
# • `list()` 인스턴스 메서드로 출석자 명단 출력.

class Student():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
        
class Attendance():
    def __init__(self):
        self.students = []
    def attend(self, student):
        self.students.append(student)
    def list(self):
        return self.students