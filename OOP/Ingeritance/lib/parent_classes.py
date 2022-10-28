
class Person(object):
    def __init__(self, name: str, age: int, email: str, phone: str, address: str):
        self._age = age
        self._name = name
        self._email = email
        self._phone = phone
        self._address = address

    def __str__(self):
        return f'{self._name} - {self._age} years; {self._email}; {self._phone}; {self._address}'

