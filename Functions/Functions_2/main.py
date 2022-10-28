from demo.task_657 import demo1
from demo.task_660 import demo2
from demo.task_662 import demo3
from demo.task_674 import demo4
from demo.task_1015 import demo5
from demo.task_1026 import demo6
from examples.ex1 import read_lists_from_file


if __name__ == '__main__':

    print('1 - 657')
    print('2 - 660')
    print('3 - 662')
    print('4 - 674')
    print('5 - 10.15')
    print('6 - 10.26')
    print('7 - ex1')
    print('---------')

    k = int(input('Виберіть задачу: '))

    if k == 1:
        demo1()
    elif k == 2:
        demo2()
    elif k == 3:
        demo3()
    elif k == 4:
        demo4()
    elif k == 5:
        demo5()
    elif k == 6:
        demo6()
    elif k == 7:
        read_lists_from_file()
    else:
        print('Ви ввели неіснуючий варіант вибору')
