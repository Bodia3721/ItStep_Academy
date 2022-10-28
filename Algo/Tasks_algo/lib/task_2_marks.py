# Заданий масив оцінок студентів. За допомогою функцій вищих
# порядків потрібно збільшити оцінку кожного студента на 1 бал
# та відібрати після цього оцінки, вищі від 6 балів.

marks = [5, 7, 8, 11, 9, 7, 4, 10, 5, 3, 5, 6, 9]

if __name__ == '__main__':

    new_marks = list(map(lambda x: x+1, marks))
    print(new_marks)
    sorted_marks = list(filter(lambda x: x > 6, new_marks))
    print(sorted_marks)
