class Student(object):

    def __init__(self, name: str, surname: str, age: int, rate: float):
        self._name = name
        self._surname = surname
        self._age = age
        self._rate = rate

    def __str__(self) -> str:
        return f'{self._name} {self._surname} - {self._age} yeas; rate: {self._rate}'


class Group(object):

    def __init__(self, name: str):
        self._name = name
        self._students = []

    def add_student(self, student: Student) -> None:
        self._students.append(student)

    def display_students(self) -> None:
        print('Група:', self._name)
        print('Студентів:', len(self._students))
        k = 0
        for student in self._students:
            k += 1
            print(f'{k}. {student}')
