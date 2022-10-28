def read_lists_from_file() -> None:
    with open('ex1.txt', 'r') as fr:
        row1 = fr.readline().split()
        row2 = fr.readline().split()

    list1 = [int(item) for item in row1]
    list2 = row2

    print(row1)
    print(list1)
    print(list2)
