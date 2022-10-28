from lib.list_functions import copy_list, fill_list, display_list
from lib.task_1_bubble import new_bubble_sort, bubble_sort
from lib.task_3_677 import square_root_funcs

if __name__ == '__main__':

    n = 10
    x = [0] * n
    a = [0] * n
    b = [0] * n

    fill_list(x)
    copy_list(x, a)
    copy_list(x, b)

    new_bubble_sort(a)
    bubble_sort(b)

    print('Example list: ')
    display_list(x)
    print('New Bubble sort: ')
    display_list(a)
    print('Classic Bubble sort: ')
    display_list(b)

    num = 25
    print('----------------------------------------')
    print(f'Square root of {num} : {square_root_funcs(num)}')
