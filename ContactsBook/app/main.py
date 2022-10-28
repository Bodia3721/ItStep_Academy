from lib.menu import Menu
from lib.services import *


if __name__ == '__main__':

    menu = Menu()
    service1 = CategoriesService()
    service2 = ContactsService()

    while True:
        menu.show_menu()
        menu.make_choice()

        if menu.choice == 1:
            service1.print_categories_list()
        elif menu.choice == 2:
            pass
        elif menu.choice == 3:
            service1.add_category_dialog()
        elif menu.choice == 4:
            service1.edit_category_dialog()
        elif menu.choice == 5:
            service1.del_category_dialog()
        elif menu.choice == 6:
            service2.print_contacts_list()
        elif menu.choice == 7:
            service2.add_contact_dialog()
        elif menu.choice == 8:
            service2.edit_contact_dialog()
        elif menu.choice == 9:
            service2.del_contact_dialog()
        elif menu.choice == 10:
            break
        else:
            print('  Ви вказали некоректне значення')

        if not menu.allow_continue():
            break
