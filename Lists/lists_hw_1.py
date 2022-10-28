#---------------Домашнее задание--Задание №1-----------------

# letters = []
#
# while True:
#     x = input('Enter the letter: ')
#     if x == '':
#         break
#     letters.append(x)
#
# letter_count = 0
#
# for i in letters:
#     letter_count += 1
# print('The count of letters is ', letter_count)

#---------------Домашнее задание--Задание №2-----------------
list_of_items = ['apple', 'orange', 'banana', 'juice']

while True:
    x = input('Enter the items: ')
    if x in list_of_items:
        print('You have already bought ' + x)
        list_of_items.remove(x)
    else:
        print(x + ' is not in the list of items!' )

    if len(list_of_items) == 0:
        print('You have already bought all items!')
        break
