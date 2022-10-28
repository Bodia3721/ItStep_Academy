# 1015
def is_prime(x: int) -> bool:
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

# 7
# 2, 3, 4, 5, 6
