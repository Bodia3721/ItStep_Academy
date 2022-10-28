from lib.parent_classes import *
from lib.child_classes import *
from lib.teacher_classes import *
from lib.manager_classes import *

if __name__ == '__main__':
    person1 = Person('Vasya Nikonov', 21, 'vasya@gmail.com', '1111-11-11', 'Kyiv')
    print(person1)

    student1 = Student('Mykola Laskov', 18, 'kolya@gmail.com', '2222-22-22', 'Lviv', 9.8, 'IPS-21')
    print(student1)

    teacher1 = Teacher('Anna Kot', 35, 'kot@gmail.com', '3333-33-33', 'Lviv', 8, 800)
    print(teacher1)

    manager1 = Manager('Olga Petrenko', 29, 'olga@gmail.com', '4444-44-44', 'Odessa', 'Sales', 1100)
    print(manager1)
