from lib.repositories import GroupRepository
from lib.models import Student


class GroupService(object):

    def __init__(self, repo: GroupRepository):
        self._repo = repo

    def create_new_student(self) -> None:
        print('Додавання нового студента')
        print('-------------------------')
        #
        name = input("Введіть ім'я: ")
        surname = input("Введіть прізвище: ")
        age = int(input("Введіть вік: "))
        rate = float(input("Введіть рейтинг: "))
        #
        new_student = Student(name, surname, age, rate)
        self._repo.group.add_student(new_student)
        self._repo.save_data()
        print('Студент успішно створений. Персональні дані збережені')

    def search_student(self):
        print('Пошук студента в групі')
        print('----------------------')
        #
        name = input("Введіть ім'я: ")
        surname = input("Введіть прізвище: ")
        self._repo.group.find_student(name, surname)

