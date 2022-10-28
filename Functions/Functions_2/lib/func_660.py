def check_ideal(n: int) ->bool:
    """Функція на перевірку чи ідеальне число"""
    s = 0
    for x in range(1, n):
        if n % x == 0:
            s += x
    return n == s