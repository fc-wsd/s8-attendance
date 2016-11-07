import unittest

class Student:

    def __init__(self, _name):
        self.name = _name
    def __str__(self):
        return self.name

class Attendance:

    def __init__(self):
        self.student_list = []
    
    def attend(self, student):
        self.student_list.append(student)

    def list(self):
        name_list = [];
        for student in self.student_list:
            name_list.append(student.name)
        return name_list

class TestModule(unittest.TestCase):

    def test_student_str_is_his_name(self):
        s = Student('kang')
        self.assertEqual(str(s), 'kang')

    def test_one_student_attend_list_shows_his_name(self):
        s = Student('kang')
        attendance = Attendance()
        attendance.attend(s)
        self.assertEqual(attendance.list(), ['kang'])

    def test_two_students_attend_list_shows_list_with_two(self):
        s1 = Student('kang')
        s2 = Student('kim')
        attendance = Attendance()
        attendance.attend(s1)
        attendance.attend(s2)
        self.assertEqual(attendance.list(), ['kang', 'kim'])

    def test_list_equal(self):
        l1 = ['kang', 'kim']
        l2 = ['kim', 'kang']
        self.assertEqual(l1, l2[::-1])

if __name__ == '__main__':
    unittest.main()
