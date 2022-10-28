def display_list(x: list) -> None:
    for elem in x:
        print(elem, end=' ')
    print()


def fill_list(x: list) -> None:
    import random
    for i in range(len(x)):
        x[i] = random.randint(10, 99)


def copy_list(x: list, y: list) -> None:
    for i in range(len(x)):
        y[i] = x[i]
