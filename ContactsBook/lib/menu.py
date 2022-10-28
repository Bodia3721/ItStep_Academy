class Menu(object):

    def __init__(self):
        self._choice = 0

    @property
    def choice(self) -> int:
        return self._choice

    @staticmethod
    def show_menu() ->None:
        print('\t ===============================')
        print('\t  Система управління контактами')
        print('\t ===============================')
        print('\t 1. Вивести список категорій')
        print('\t 2. Контакти по категоріям')
        print('\t 3. Додати нову категорію')
        print('\t 4. Відредагувати категорію')
        print('\t 5. Видалити категорію')
        print('\t 6. Вивести список контактів')
        print('\t 7. Додати новий контакт')
        print('\t 8. Відредагувати контакт')
        print('\t 9. Видалити контакт')
        print('\t 10.Вийти із програми')
        print('\t ===============================')

    def make_choice(self) -> None:
        try:
            self._choice = int(input('>Виберіть номер потрібної операції: '))
        except ValueError as error:
            print(f'  Виключення: {error}')
            self._choice=0

    @staticmethod
    def allow_continue() -> bool:
        answer = input('\n>Продовжити (y/n)? - ')
        return answer == 'y'
