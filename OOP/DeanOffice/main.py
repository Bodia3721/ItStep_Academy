from lib.models import Student, Group, Faculty
from lib.repositories import GroupRepository, FacultyRepository
from lib.services import GroupService



if __name__ == '__main__':

    group1 = Group('Group-Py-01')
    vasya = Student('Василь', 'Татаренко', 21, 8.6)
    kolya = Student('Микола', 'Маханько', 19, 7.9)
    katya = Student('Катя', 'Ніконова', 20, 8.2)

    group2 = Group('Group-Py-02')
    dima = Student('Дмитро', 'Костенко', 18, 9.7)
    stas = Student('Станіслав', 'Бойко', 18, 8.5)
    misha = Student('Михайло', 'Пушко', 18, 9.0)
    maks = Student('Максим', 'Рама', 21, 9.3)


    faculty1 = Faculty("Комп'ютерних наук", group1)
    persons_1 = [vasya, kolya, katya]
    for p in persons_1:
        group1.add_student(p)
        faculty1.add_student(p)
    # faculty1.display_groups()
    # f_repo1 = FacultyRepository(faculty1)
    # f_repo1.save_data()

    faculty2 = Faculty("Комп'ютерних наук", group2)
    persons_2 = [dima, stas, misha, maks]
    for p in persons_2:
        group2.add_student(p)
        faculty2.add_student(p)

    # faculty2.display_groups()
    # f_repo2 = FacultyRepository(faculty1)
    # f_repo2.save_data()

    #group1.display_students()

    repo1 = GroupRepository(group1)
    #repo1.save_data()
    repo1.load_data()

    service = GroupService(repo1)
    #service.create_new_student()
    repo1.group.display_students()
    service.search_student()






