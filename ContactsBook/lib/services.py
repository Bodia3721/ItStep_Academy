from lib.repos import *


class CategoriesService(object):

    def __init__(self):
        self._repos = CategoriesRepository()

    def print_categories_list(self):
        for category in self._repos.get_all_categories():
            print(category)

    def add_category_dialog(self):
        category_name = input('  Введіть назву нової категорії: ')
        self._repos.add_new_category(category_name)
        print('  Категорія успішно створена')

    def edit_category_dialog(self):
        exist_category_name = input('  Введіть назву категорії для редагування: ')
        edit_category_name = input('  Введіть нову назву: ')
        self._repos.edit_exist_category(exist_category_name, edit_category_name)
        print('  Назва категорії успішно змінена')

    def del_category_dialog(self):
        exist_category_name = input('  Введіть назву категорії для видалення: ')
        self._repos.del_exist_category(exist_category_name)
        print('  Категорію успішно видалено')


class ContactsService(object):

    def __init__(self):
        self._repos = ContactsRepository()

    def print_contacts_list(self):
        for contact in self._repos.get_all_contacts():
            print(contact)

    def add_contact_dialog(self):
        new_contact_name = input("  Введіть ім'я нового контакту: ")
        new_contact_email = input("  Введіть e-mail нового контакту: ")
        new_contact_phone = input("  Введіть телефон нового контакту: ")
        new_contact_telegram = input("  Введіть телеграм нового контакту: ")
        new_category_id = int(input("  Введіть ID категорії: "))
        self._repos.add_new_contact(new_contact_name, new_contact_email, new_contact_phone,
                                    new_contact_telegram, new_category_id)
        print('  Контакт успішно створений')

    def edit_contact_dialog(self):
        exist_contact_name = input("  Введіть ім`я контакту для видалення: ")
        edit_contact_email = input("  Введіть e-mail: ")
        edit_contact_phone = input("  Введіть телефон: ")
        edit_contact_telegram = input("  Введіть телеграм: ")
        edit_category_id = int(input("  Введіть ID категорії: "))
        self._repos.edit_exist_contact(exist_contact_name, edit_contact_email, edit_contact_phone,
                                       edit_contact_telegram, edit_category_id)
        print('  Зміни успішно збережено')

    def del_contact_dialog(self):
        exist_contact_name = input("  Введіть ім'я контакту для видалення: ")
        self._repos.del_exist_contact(exist_contact_name)
        print('  Контакт успішно видалено')