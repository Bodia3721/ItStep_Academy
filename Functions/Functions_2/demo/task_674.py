# 674
from lib.func_674 import frequency


def demo4() -> None:
    with open('input4.txt', 'r') as fr:
        content = fr.readline().split(',')

    numbers = [int(x) for x in content]
    result = frequency(numbers)

    print(result)
    with open('output.txt', 'w') as fw:
        fw.write(str(result))

    print('task-674 done OK')
