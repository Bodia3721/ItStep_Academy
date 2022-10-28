from lib.menu import *
from data.data import *


if __name__ == '__main__':

    data = load_all_data()
    size = len(data['departments'])
    exit_flag = False

    while True:
        display_menu()
        k = get_choice()

        if k == 1:
            display_departments(data)
        elif k == 2:
            dep_number = int(input('Виберіть номер департамента: '))
            if dep_number in range(1, size + 1):
                display_employees(data, dep_number)
        elif k == 3:
            dep_number = int(input('Виберіть номер департамента: '))
            emp_number = int(input('Виберіть номер співробітника: '))
            if dep_number in range(1, size + 1):
                display_employee_info(data, dep_number, emp_number)
        elif k == 4:
            name = input('Введіть ПІБ працівника: ')
            employee_search(data, name)
        elif k == 5:
            pass
        elif k == 6:
            pass
        elif k == 7:
            pass
        elif k == 8:
            pass
        elif k == 9:
            pass
        elif k == 10:
            pass
        elif k == 11:
            exit_flag = True
        else:
            print('Ви ввели некоректне значення')

        if exit_flag or not allow_continue():
            break

    print('Програма завершена')
