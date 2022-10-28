from time import time


def fill_list(x: list) -> None:
    import random
    for i in range(len(x)):
        x[i] = random.randint(10, 99)


def copy_list(x: list, y: list) -> None:
    for i in range(len(x)):
        y[i] = x[i]


def time_monitor(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        finish = time()
        duration = round((finish - start) * 1000, 5)
        print(f'Execution time: {duration} ms')
    return wrapper


@time_monitor
def bubble_sort(x: list) -> None:
    n = len(x)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]


@time_monitor
def selection_sort(x: list) -> None:
    n = len(x)
    for i in range(n - 1):
        m = x[i]
        k = i
        for j in range(i + 1, n):
            if x[j] < m:
                m = x[j]
                k = j
        x[i], x[k] = x[k], x[i]


@time_monitor
def insertion_sort(x: list) -> None:
    n = len(x)
    for i in range(1, n):
        if x[i] < x[i - 1]:
            buff = x[i]
            j = i - 1
            while x[j] > buff and j >= 0:
                x[j + 1] = x[j]
                j -= 1
            x[j + 1] = buff


def quick_sort_rec(x: list, left: int, right: int):
    if left < right:
        p = x[(left + right) // 2]
        i = left
        j = right
        while i <= j:
            while x[i] < p:
                i += 1
            while x[j] > p:
                j -= 1
            if i < j:
                x[i], x[j] = x[j], x[i]
            if i <= j:
                i += 1
                j -= 1
        quick_sort_rec(x, left, j)
        quick_sort_rec(x, i, right)


@time_monitor
def quick_sort(x: list) -> None:
    n = len(x)
    quick_sort_rec(x, 0, n - 1)


if __name__ == '__main__':
    size = int(input('Set the size of the array: '))

    x = [0] * size
    a = [0] * size
    b = [0] * size
    c = [0] * size
    d = [0] * size

    fill_list(x)
    copy_list(x, a)
    copy_list(x, b)
    copy_list(x, c)
    copy_list(x, d)

    print('------------------Bubble sort------------------')
    bubble_sort(a)
    print('------------------Selection sort------------------')
    selection_sort(b)
    print('------------------Insertion sort------------------')
    insertion_sort(c)
    print('------------------Quick sort------------------')
    quick_sort(d)






