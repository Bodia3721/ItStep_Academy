class Employee(object):

    def __init__(self, name: str, age: int, position: str, salary: float):
        self._name = name
        self._age = age
        self._position = position
        self._salary = salary

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, salary: float) -> None:
        self._salary = salary


if __name__ == '__main__':

    emp = Employee('Ліза Пупкіна', 23, 'Дизайнер', 1600)

    print('name:', emp.name)
    print('age:', emp.age)
    print('salary:', emp.salary)

    emp.salary = emp.salary + 400
    print('new_salary:', emp.salary)
