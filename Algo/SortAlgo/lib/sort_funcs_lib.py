def bubble_sort(x: list) -> None:
    n = len(x)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]


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


def quick_sort(x: list) -> None:
    n = len(x)
    quick_sort_rec(x, 0, n - 1)
