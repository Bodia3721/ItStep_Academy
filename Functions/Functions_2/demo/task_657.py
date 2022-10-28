# 657
from lib.func_657 import my_pow

def demo1() -> None:
    with open('input1.txt', 'r') as fr:
       a1 = float(fr.readline())
       n1 = int(fr.readline())
       a2 = float(fr.readline())
       n2 = int(fr.readline())

    res1 = my_pow(a1, n1)
    res2 = my_pow(a2, n2)

    print(res1)
    print(res2)

    with open('output.txt', 'w') as fw:
        fw.write(f'{round(res1, 1)}\n')
        fw.write(f'{round(res2, 1)}')
