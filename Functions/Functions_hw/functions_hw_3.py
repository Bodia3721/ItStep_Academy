from math import sqrt

def square_calc():
    if figure == 'triangle':
        a = int(input('Enter a: '))
        b = int(input('Enter b: '))
        c = int(input('Enter c: '))
        if triangle_check(a, b, c) is True:
            triangle_square(a, b, c)
        else:
            print('Such a figure does not exist')
    elif figure == 'circle':
        r = int(input('Enter r: '))
        if circle_check(r) is True:
            circle_square(r)
        else:
            print('Such a figure does not exist')
    elif figure == 'rectangle':
        a = int(input('Enter a: '))
        b = int(input('Enter b: '))
        if rectangle_check(a, b) is True:
            rectangle_square(a, b)
        else:
            print('Such a figure does not exist')
    else:
        print('Choose the correct figure!')


def triangle_square(a, b, c)-> float:
    p = (a + b + c) / 2
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    print(f'Triangle square: {round(s)}')

def circle_square(r)-> float:
    s = 3.14 * r
    print(f'Circle square: {round(s)}')

def rectangle_square(a, b)-> float:
    s = a * b
    print(f'Rectangle square: {round(s)}')

def triangle_check(a, b, c) -> bool:
    if a + b> c and a + c> b and b + c> a and a> 0 and b> 0 and c> 0:
            return True
    else:
        return False

def circle_check(r) -> bool:
    if r > 0:
        return True
    else:
        return False

def rectangle_check(a, b) -> bool:
    if a > 0 and b > 0:
        return True
    else:
        return False


if __name__ == '__main__':
    figure = input('Choose the name of figure (triangle, circle, rectangle):' )
    square_calc()
