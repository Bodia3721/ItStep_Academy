class Student(object):

    def __init__(self, name: str, surname: str, age: int, rate: float):
        self._name = name
        self._surname = surname
        self._age = age
        self._rate = rate

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    def __str__(self) -> str:
        return f'{self._name} {self._surname} - {self._age} years; rate: {self._rate}'


class Group(object):

    def __init__(self, gname: str):
        self._gname = gname
        self._students = []

    def add_student(self, student: Student) -> None:
        self._students.append(student)

    def display_students(self) -> None:
        print('Група:', self._gname)
        print('Студентів:', len(self._students))
        k = 0
        for student in self._students:
            k += 1
            print(f'{k}. {student}')

    def find_student(self, name: str, surname: str) -> None:
        success_find = False
        for student in self._students:
            if student.name == name and student.surname == surname:
                success_find = True
                print('Студента знайдено')
                print(student)
                break
        if not success_find:
            print('Студента не знайдено')




class Faculty(object):

    def __init__(self, name: str, gname):
        self._name = name
        self._students = []
        self._gname = gname


    def __str__(self):
        return self._name

    def add_student(self, student: Student) -> None:
        self._students.append(student)

    def display_groups(self):
        print('Факультет', self._name)
        self._gname.display_students()
