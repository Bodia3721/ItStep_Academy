print("Select the action you want to do: +, -, /, * ")

action = input("Action:")
if action in ('+', '-', '*', '/'):
    x = float(input('x = '))
    y = float(input('y = '))

    if action == '+':
        print('x + y =', x+y)
    elif action == '-':
        print('x - y =', x-y)
    elif action == '*':
        print('x * y =', x*y)
    elif action == '/':
        if y != 0:
            print('x / y =', x / y)
        else:
            print("Can't divide by 0")

