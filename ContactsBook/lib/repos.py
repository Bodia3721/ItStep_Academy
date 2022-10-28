from lib.providers import SQLiteProvider
from lib.models import *


class CategoriesRepository(SQLiteProvider):

    def __init__(self):
        super().__init__('contacts.db')
        self._categories = []
        self.load_data()

    def load_data(self):
        result = self._cursor.execute('select * from Categories').fetchall()  # [(1,..), (2,..), ()] -> [m1, m2, m3]
        self._categories.clear()
        for category_tuple in result:
            category_model = CategoryModel(category_tuple[0], category_tuple[1])
            self._categories.append(category_model)

    def get_all_categories(self):
        return self._categories

    def add_new_category(self, new_category_name: str):
        new_category_id = self._categories[-1].category_id+1
        new_category_model = CategoryModel(new_category_id, new_category_name)
        self._categories.append(new_category_model)
        #
        self._cursor.execute('insert into Categories (category_name) values (?)', (new_category_name,))
        self._connection.commit()

    def edit_exist_category(self, exist_category_name: str, edit_category_name: str):
        for category in self._categories:
            if category.category_name == exist_category_name:
                category.category_name = edit_category_name

        self._cursor.execute('update Categories set category_name=? where category_name=?',
                             (edit_category_name, exist_category_name))
        self._connection.commit()

    def del_exist_category(self, exist_category_name: str):

        for category in self._categories:
            if category.category_name == exist_category_name:
                self._categories.remove(category)

        self._cursor.execute('delete from Categories where category_name=?', (exist_category_name,))
        self._connection.commit()


class ContactsRepository(SQLiteProvider):

    def __init__(self):
        super().__init__('contacts.db')
        self._contacts = []
        self.load_data()

    def load_data(self):
        result = self._cursor.execute('select * from Contacts').fetchall()
        self._contacts.clear()
        for contacts_tuple in result:
            contact_model = ContactModel(contacts_tuple[0], contacts_tuple[1], contacts_tuple[2], contacts_tuple[3],
                                         contacts_tuple[4], contacts_tuple[5])
            self._contacts.append(contact_model)

    def get_all_contacts(self):
        return self._contacts

    def add_new_contact(self, new_contact_name: str, new_contact_email: str, new_contact_phone: str,
                        new_contact_telegram: str, new_category_id: int):
        new_contact_id = self._contacts[-1].contact_id+1
        new_contact_model = ContactModel(new_contact_id, new_contact_name, new_contact_email, new_contact_phone,
                                         new_contact_telegram, new_category_id)
        self._contacts.append(new_contact_model)

        self._cursor.execute("""
            insert into Contacts
                (contact_name, contact_email, contact_phone, contact_teleg, category_id)
            values
                (?,?,?,?,?)
            """, (new_contact_name, new_contact_email, new_contact_phone, new_contact_telegram, new_category_id))
        self._connection.commit()

    def edit_exist_contact(self, exist_contact_name: str, edit_contact_email: str, edit_contact_phone: str,
                        edit_contact_telegram: str, edit_category_id: int):
        for contact in self._contacts:
            if contact.contact_name == exist_contact_name:
                contact.contact_email = edit_contact_email
                contact.contact_phone = edit_contact_phone
                contact.contact_telegram = edit_contact_telegram
                contact.category_id = edit_category_id

        self._cursor.execute("""
            update Contacts
                set contact_email=?, contact_phone=?, contact_teleg=?, category_id
                where contact_name=?
        """, (edit_contact_email, edit_contact_phone, edit_contact_telegram, edit_category_id, exist_contact_name))
        self._connection.commit()

    def del_exist_contact(self, exist_contact_name):
        for contact in self._contacts:
            if contact.contact_name == exist_contact_name:
                self._contacts.remove(contact)

        self._cursor.execute('delete from Contacts where contact_name=?', (exist_contact_name,))
        self._connection.commit()

