from json import load, dump

import data


def load_all_data() -> dict:
    with open('hr.json', 'r', encoding='utf-8') as file:
        data = load(file)
    return data


def upload_all_data(data: dict) -> None:
    with open('hr.json', 'w', encoding='utf-8') as file:
        dump(data, file)
    print('Дані успішно збережені')


def display_departments(data: dict) -> None:
    print('----------------------')
    print(f'  {data["company"]}')
    print('----------------------')
    k = 1
    for dep in data['departments']:
        print(f'{k}. {dep["dep_name"]}')
        k += 1
    print('----------------------')


def display_employees(data: dict, dep_number: int) -> None:
    print('---------------------')
    print(f'  {data["departments"][dep_number - 1]["dep_name"]}')
    print('---------------------')
    k = 1
    for emp in data["departments"][dep_number - 1]["employees"]:
        print(f'{k}. {emp["emp_name"]}')
        k += 1


def display_employee_info(data: dict, dep_number: int, emp_number: int) -> None:
    dep = data['departments'][dep_number - 1]
    emp = dep['employees'][emp_number - 1]
    name = emp['emp_name']
    pos = emp['emp_position']
    age = emp['emp_age']
    salary = emp['emp_salary']
    print(f'{name} - {pos}; {age} років; {salary} usd')


def employee_search(data: dict, name: str):
    for x in data['departments']:
        for y in x['employees']:
            if y['emp_name'] == name:
                print(f"{y['emp_name']} - {y['emp_position']}; {y['emp_age']} років; {y['emp_salary']} usd ")

