# Напишіть окрему версію функції для сортування масивів
# бульбашковим алгоритмом, але у зворотному порядку.

def new_bubble_sort(x: list) -> None:
    n = len(x)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if x[j] < x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]


def bubble_sort(x: list) -> None:
    n = len(x)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]