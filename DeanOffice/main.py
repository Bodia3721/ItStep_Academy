from lib.models import Student, Group
from lib.repositories import GroupRepository
from lib.services import GroupService


if __name__ == '__main__':

    # 1 група:
    group1 = Group('Group-Py-123')
    group1.display_students()

    repo = GroupRepository(group1)
    repo.load_data()

    service = GroupService(repo)
    service.create_new_student()

    repo.load_data()
    repo.group.display_students()
