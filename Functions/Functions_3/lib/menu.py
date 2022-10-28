def display_menu() -> None:
    print('---------------------------------------------')
    print(' Система управління відділом кадрів компанії ')
    print('---------------------------------------------')
    print('     1 - Перегляд списку департаментів       ')
    print('     2 - Перегляд списку співробітників      ')
    print('     3 - Перегляд персональної інформації    ')
    print('     4 - Пошук співробітників в базі         ')
    print('     5 - Додавання співробітника             ')
    print('     6 - Видалення співробітника             ')
    print('     7 - Редагування співробітника           ')
    print('     8 - Переведення співробітника           ')
    print('     9 - Додавання департаменту              ')
    print('    10 - Видалення департаменту              ')
    print('    11 - Вихід із програми                   ')
    print('---------------------------------------------')


def get_choice() -> int:
    try:
        choice = int(input('Виберіть номер потрібної дії: '))
    except ValueError:
        choice = 0
    return choice


def allow_continue() -> bool:
    allow = input('Продовжити (y/n)? - ')
    return allow == 'y'