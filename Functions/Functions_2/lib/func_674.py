# 674
def frequency(numbers: list) -> list():
    result = []
    unique_set = set(numbers)
    unique_list = list(unique_set)

    for x in unique_list:
        n = numbers.count(x)
        t = (x, n)
        result.append(t)

    return result
