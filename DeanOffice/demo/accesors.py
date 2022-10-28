class Employee(object):

    def __init__(self, name: str, age: int, position: str, salary: float):
        self._name = name
        self._age = age
        self._position = position
        self._salary = salary

    def get_name(self) -> str:
        return self._name

    def get_age(self) -> int:
        return self._age

    def get_salary(self) -> float:
        return self._salary

    def set_salary(self, salary: float) -> None:
        self._salary = salary


if __name__ == '__main__':

    emp = Employee('Василь Пупкін', 21, 'Кодер', 1500)

    print('name:', emp.get_name())
    print('age:', emp.get_age())
    print('salary:', emp.get_salary())

    emp.set_salary(emp.get_salary() + 300)
    print('new_salary:', emp.get_salary())
