
class User(object):

    def __init__(self, first_name: str, last_name: str, login_attempts: int =0, age: int = 0, phone: str = ''):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._phone = phone
        self._login_attempts = login_attempts

    @property
    def login_attempts(self):
        return self._login_attempts

    def describe_user(self):
        print(f'User name: {self._first_name} {self._last_name}')

    def greeting_user(self):
        print(f'Congratulations {self._first_name}! Good day to you!!!\n')

    def increment_login_attempts(self):
        self._login_attempts += 1

    def reset_login_attempts(self):
        self._login_attempts = 0


class Admin(User):

    def __init__(self, first_name: str, last_name: str, priv: list):
        super().__init__(first_name, last_name)
        self._priv = priv

    @property
    def priv(self):
        return self._priv


class Privileges(object):

    def __init__(self, privileges: list):
        self._privileges = privileges

    @property
    def privileges(self):
        return self._privileges

    def show_privileges(self):
        for p in self._privileges:
            print(p)


if __name__ == '__main__':

    # a
    user1 = User('Andriy', 'Shevchenko')
    user2 = User('Oleksandr', 'Zinchenko')
    user3 = User('Andriy', 'Pyatov')

    users = [user1, user2, user3]
    for i in users:
        i.describe_user()
        i.greeting_user()

    # b
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    print(f'Login attempts: {user1.login_attempts}')
    user1.reset_login_attempts()
    print(f'Login attempts: {user1.login_attempts}')

    # c
    print('\n---------Admin----------')
    admin = Admin('Head', 'admin', ['Allowed to add message', 'Allowed to delete users', 'Allowed to ban users'])
    # admin.show_privileges()

    # d
    admin2 = Privileges([])
    for i in admin.priv:
        admin2.privileges.append(i)

    admin2.show_privileges()

