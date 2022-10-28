from lib.models import Group, Faculty
from pickle import dump, load


class GroupRepository(object):
    """ DI - Dependency Injection (Вбудовування залежності) """

    def __init__(self, group: Group):
        self._group = group

    @property
    def group(self):
        return self._group

    def save_data(self) -> None:
        with open('group1.dat', 'wb') as file:
            dump(self._group, file)
        print('Дані успішно збережені')

    def load_data(self) -> None:
        with open('group1.dat', 'rb') as file:
            self._group = load(file)
        print('Дані успішно завантажені')


class FacultyRepository(object):

    def __init__(self, faculty: Faculty):
        self._faculty = faculty

    @property
    def faculty(self):
        return self._faculty

    def save_data(self) -> None:
        with open('faculty1.dat', 'wb') as file:
            dump(self._faculty, file)
        print('Дані успішно збережені')
