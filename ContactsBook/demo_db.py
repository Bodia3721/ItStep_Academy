from sqlite3 import *


def data_adapter(table_name, data: list):
    print(f'\n>{table_name}')
    for row in data:
        for item in row:
            print(f'{item}', end='  ')
        print()


if __name__ == '__main__':
    print('Книга контактів')

    connection = connect('contacts.db')
    cursor = connection.cursor()

    # name = input("Введіть ім'я: ")
    # email = input("Введіть імейл: ")
    # phone = input("Введіть телефон: ")
    # telegram = input("Введіть телеграм: ")
    # c_id = int(input("Ввідеть ID категорії: "))
    # cursor.execute("""
    #     insert into Contacts
    #         (contact_name, contact_email, contact_phone, contact_teleg, category_id)
    #     values
    #         (?,?,?,?,?)
    # """, (name, email, phone, telegram, c_id))
    # connection.commit()
    # print('Контакт успішно збережено')
    #
    # data_adapter('Categories', cursor.execute('select * from Categories').fetchall())
    data_adapter('Contacts', cursor.execute('select * from Contacts').fetchall())


    # Редагування даних
    contact_id = input('Введіть ID контакта для зміни даних: ')
    phone = input("Введіть телефон: ")
    telegram = input("Введіть телеграм: ")
    cursor.execute("""
        update Contacts
            set contact_phone= ?, contact_teleg=?
            where contact_id=?
    """, (phone, telegram, contact_id))
    connection.commit()

    data_adapter('Contacts', cursor.execute('select * from Contacts').fetchall())