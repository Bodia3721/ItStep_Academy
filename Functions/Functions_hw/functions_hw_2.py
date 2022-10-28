from math import sqrt
#653
# Input:
# 1 0 7 8 10
# 3 2 6 4 3

def check_list() -> bool:
    with open('input.txt', 'r') as fr:
        s1 = str(fr.readline())
        s2 = str(fr.readline())

    l1 = s1.split()
    l2 = s2.split()

    for i in l1:
       if i in l2:
           print(True)


#648

def calc_distance() ->float:
    with open('input.txt', 'r') as fr:
        x1 = int(fr.readline())
        y1 = int(fr.readline())
        x2 = int(fr.readline())
        y2 = int(fr.readline())

    distance = sqrt((x1-x2)**2 + (y1-y2)**2)
    print(round(distance, 5))


if __name__ == '__main__':

    check_list()
    calc_distance()