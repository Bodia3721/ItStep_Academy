from time import time, sleep

def decorator1(target_func):
    def wrapper_func():
        print('#Дії декоратора-1 перед викликом цільової функції')
        target_func()
        print('#Дії декоратора-1 після виклику цільової функції')

    return wrapper_func


def decorator2(target_func):
    def wrapper_func():
        print('##Дії декораторас-2 перед викликом цільової функції')
        target_func()
        print('##Дії декоратора-2 після виклику цільової функції')

    return wrapper_func


def universal_sum(*args, **kwargs) -> float:
    '''
        *args - колекція позиційних аргументів
        **kwargs - колекція ключових аргументів
    '''
    return args, kwargs


@decorator1
@decorator2
def target_func():
    print('Довільна цільова функція виконує певні дії...')


def time_monitor(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        finish = time()
        duration = round((finish - start) * 1000, 3)
        print(f'Час виконання: {duration} мс')
    return wrapper


@time_monitor
def test(duration: float):
    sleep(duration)

if __name__ == '__main__':

    #target_func()
    #print(universal_sum(10, 20, 50, num1=111, num2=222))
    test(1.75)
    print('finish')