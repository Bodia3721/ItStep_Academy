from lib.list_funcs_lib import *
from lib.sort_funcs_lib import *


if __name__ == '__main__':

    n = 15

    x = [0] * n
    a = [0] * n
    b = [0] * n
    c = [0] * n
    d = [0] * n

    fill_list(x)
    copy_list(x, a)
    copy_list(x, b)
    copy_list(x, c)
    copy_list(x, d)

    bubble_sort(a)
    selection_sort(b)
    insertion_sort(c)
    quick_sort(d)

    print('Example list: ')
    display_list(x)
    print('Bubble sort: ')
    display_list(a)
    print('Selection sort:')
    display_list(b)
    print('Insertion sort: ')
    display_list(c)
    print('Quick sort: ')
    display_list(d)
