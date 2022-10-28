# 662
from lib.func_662 import analyze


def demo3() -> None:
    with open('input3.txt', 'r') as fr:
        content = fr.readline().split()

    grades = [int(x) for x in content]
    result = analyze(grades)

    print(result)
    with open('output.txt', 'w') as fw:
        fw.write(str(result))

    print('task-662 done OK')
