import random


def MillerRabin(p, repeat=5):
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    r = 0
    s = p - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for count in range(repeat):
        a = random.randrange(2, p - 1)
        x = pow(a, s, p)
        if x == 1 or x == p - 1:
            continue
        for count in range(r - 1):
            x = pow(x, 2, p)
            if x == p - 1:
                break
        else:
            return False
    return True