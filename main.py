import random


def MillerRabin(p, repeat= 5):
    """
    :param p: prime number
    :param repeat: number of rounds of simplicity check
    :return: 'True' if the number is prime or 'False' if the number is not prime
    """
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
    """
    :param keysize: bit length of a prime number
    :return: random prime
    """
    while True:
        num = random.getrandbits(keysize)
        if MillerRabin(num, repeat = 5):
            return num

def CoprimeTest(num1, num2):
    """

    :param num1: number
    :param num2: number
    :return: simplicity test result
    """
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
    """

    :param num1: prime number
    :param num2: prime number
    :return: the value of the Euler function of the product of two primes
    """
    return (num1 - 1)*(num2 - 1)

def GenerateE(phi):
    e = random.randint(1000000000, 100000000000)
    while not CoprimeTest(phi, e):
        e = random.randint(1000000000, 100000000000)
    return e


def GenerateD(phi, e):
    """
    :param phi: the value of the Euler function
    :return: secret (D) and open(e) exponents
    """
    return pow(e, -1, phi)

print(GenerateD(1111, 16))

def keygen():
    """
    selects a suitable public and private key by the entered prime numbers
    :return:
    """
    p, q = Generate_prime_number(), Generate_prime_number()
    n = p * q
    phi = Euler(p, q)
    e = GenerateE(phi)
    D = GenerateD(phi, e)
    print('Открытый ключ (e, n): \ne = ', e, '\n'
          'n = ', n, '\n'
          'Закрытый ключ (d, n): \n'
          'D = ', D, '\n'
          'n = ', n, '\n'
          )
    return n, e, D, p, q

def sec_to_dec(num: str):
    """

    :param num: binary number
    :return: decimal representation of the entered number
    """
    dec = 0
    j = 1
    for i in num:
        dec += int(i) * pow(2, len(num)-j)
        j += 1
    return dec

def Encrypt(message):
    emessage = ""
    for i in message:
        i = ord(i)
        i = '{0:013b}'.format(i)
        emessage += i
    emessage = "1" + emessage
    emessage = pow(int(emessage), e, n)

    return emessage

def Decrypt(emessage):
    emessage = str(pow(int(emessage), D, n))
    emessage = emessage[1:]
    count = 0
    dmessage = ''
    num = ''
    for i in emessage:
        count += 1
        num += i
        if count == 13:
            dmessage += chr((sec_to_dec(num)))
            count = 0
            num = ''

    return dmessage

def creat_electronic_signature(message):
    signature = ""
    for i in message:
        i = ord(i)
        i = '{0:013b}'.format(i)
        signature += i
    signature = "1" + signature
    signature = pow(int(signature), D, n)
    return signature

def verif_electronic_signature(signature, message):
    signature = str(pow(int(signature), D, n))
    signature = signature[1:]
    count = 0
    message_ = ''
    num = ''
    for i in signature:
        count += 1
        num += i
        if count == 13:
            message_ += chr((sec_to_dec(num)))
            count = 0
            num = ''
    if message_ == message:
        return "Verification successful!"

if __name__ == '__main__':
    while True:
        order = int(input(
            "Что вы хотите сделать? \nЗашифровать сообщение (1 на клавиатуре),\nРасшифровать (2 на клавиатуре),\nСгенерировать ключи (3 на клавиатуре),\nИспользовать электронную подпись (4 на клавиатуре): \n"))
        if order == 1:
            message = str(input('Введите исходное сообщение М: '))
            order1 = int(input('Какие ключи использовать? \n Автоматически сгенерированные (1 на клавиатуре), собственные ключи (2 на клавиатуре), ключи из файла(3 на клавиатуре): \n'))
            if order1 == 1:
                n, e, D, p, q = keygen()
            elif order1 == 2:
                p = int(input('Введите два простых числа p и q:\n'
                        'p = '))
                while not MillerRabin(p, repeat = 5):
                    p = int(input('Это не простое число. Введите другое: '))
                q = int(input('q = '))
                while not MillerRabin(p, repeat = 5):
                    q = int(input('Это не простое число. Введите другое: '))
                n = p*q
                print('n = ', n, '\n phi = ', Euler(p, q))
                e = int(input('Введите открытую экспоненту е (1 < e <= phi): e = '))
                while e not in range(2, Euler(p,q)) and not CoprimeTest(e, Euler(p, q)):
                    e = int(input('Такое число е не подходит. Введите другое: '))
            print('Шифртекст С: ', Encrypt(message))
            
        if order == 2:
            emessage = str(input('Введите шифртекст С: '))
            D = int(input('Введите закрытый ключ(D, n):\n' 'D = '))
            n = int(input('n = '))
            dmessage = Decrypt(emessage)
            print('Исходное сообщение М: ', dmessage)
        if order == 3:
            print("Получаю ключи...")
            keygen()

        if order == 4:
            order2 = int(input("Создать подпись (1 на клавитауре) или Проверить подпись (2 на клавиатуре)? \n"))
            if order2 == 1:
                message = str(input('Введите сообщение М: '))
                n, e, D, p, q = keygen()
                print('Ваша электронная подпись S: ', creat_electronic_signature(message))




