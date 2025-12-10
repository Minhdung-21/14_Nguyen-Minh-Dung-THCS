def la_so_nguyen_to(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    from math import sqrt
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True