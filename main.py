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

def Generate_prime_number(keysize = 1024):
    while True:
        num = random.getrandbits(keysize)
        if MillerRabin(num):
            return num

def CoprimeTest(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    if num1 + num2 == 1:
        return True
    else:
        return False

def Euler(num1, num2):
    phi = (num1 - 1)*(num2 - 1)
    return phi

def GeneratingD_e(phi):
    e_list = [3, 5, 17, 257, 65537]
    e = random.choice(e_list)
    while not CoprimeTest(e, phi):
        e = random.choice(e_list)
    D = pow(e, -1, phi)
    return D, e

def Encrypt(message):
    emessage = ''
    for i in message:
        C = pow(ord(i), e, n)
        emessage += (chr(C)) +
    return emessage


def Decrypt(emessage):
    demessage = ''
    n = p*q
    for i in emessage:
        M = pow(ord(i), D, n)
        demessage += chr(M)
    return demessage



