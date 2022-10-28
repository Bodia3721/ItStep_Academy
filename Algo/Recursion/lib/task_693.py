def rec_sum(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a < 0:
        return (1 + rec_sum(a, b-1))
    elif b < 0:
        return (1 + rec_sum(a-1, b))
