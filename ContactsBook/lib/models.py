

class CategoryModel(object):

    def __init__(self, category_id, category_name):
        self._category_id = category_id
        self._category_name = category_name

    def __str__(self):
        return f'{self._category_id} - {self._category_name}'

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, new_id):
        self._category_id = new_id

    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, new_name):
        self._category_name = new_name


class ContactModel(object):

    def __init__(self, contact_id, contact_name, contact_email, contact_phone, contact_telegram, category_id):
        self._contact_id = contact_id
        self._contact_name = contact_name
        self._contact_email = contact_email
        self._contact_phone = contact_phone
        self._contact_telegram = contact_telegram
        self._category_id = category_id

    def __str__(self):
        return f'{self._contact_id} - {self.contact_name}: {self._contact_email}, {self._contact_phone}, ' \
               f'{self._contact_telegram}, {self._category_id}.'

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, new_id):
        self._contact_id = new_id

    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, new_name):
        self._contact_name = new_name

    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, new_email):
        self._contact_email = new_email

    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, new_phone):
        self._contact_phone = new_phone

    @property
    def contact_telegram(self):
        return self._contact_telegram

    @contact_telegram.setter
    def contact_telegram(self, new_teleg):
        self._contact_telegram = new_teleg

    @property
    def category_id(self):
        return self._category_id

    @contact_telegram.setter
    def category_id(self, new_c_id):
        self._category_id = new_c_id
