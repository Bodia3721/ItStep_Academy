#10.15
from lib.func_1015 import is_prime


def demo5() -> None:
    k = 0
    for i in range(2, 100):
        if is_prime(i):
            # k += 1
            print(f'{i} ')
    # print(f'k = {k}')
