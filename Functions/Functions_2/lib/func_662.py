# 652
def analyze(grades: list) -> dict:
    """ Функція аналізує і розподіляє оцінки по рівнях американської системи оцінювання (A-F) """
    res = {
        'A': [],
        'B': [],
        'C': [],
        'D': [],
        'F': []
    }

    for x in grades:
        if x in range(90, 101):
            res['A'].append(x)
        elif x in range(80, 90):
            res['B'].append(x)
        elif x in range(70, 80):
            res['C'].append(x)
        elif x in range(60, 70):
            res['D'].append(x)
        elif x < 60:
            res['F'].append(x)

    return res
