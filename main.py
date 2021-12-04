import random

def MillerRabin(p, repeat = 5):
    """

    Probability test for simplicity
    https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D1%81%D1%82_%D0%9C%D0%B8%D0%BB%D0%BB%D0%B5%D1%80%D0%B0_%E2%80%94_%D0%A0%D0%B0%D0%B1%D0%B8%D0%BD%D0%B0

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
    Return suitable prime number

    :param keysize: bit length of a prime number
    :return: random prime
    """
    while True:
        num = random.getrandbits(keysize)
        if MillerRabin(num, repeat = 5):
            return num

def CoprimeTest(num1, num2):
    """
    Checks numbers for coprime

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
    Euler's function multiplicative arithmetic function,
    the value of which is equal to the number of natural numbers not exceeding n and coprime to it

    :param num1: prime number
    :param num2: prime number
    :return: the value of the Euler function of the product of two primes
    """
    return (num1 - 1)*(num2 - 1)

def GenerateE(phi):
    """
    Selects a random number e in an range (1, phi+1) such that e is coprime with phi.
    However, in order to save memory the range is reduced to (1, 100000000000).

    :param phi: the value of the Euler function
    :return: situable open (e) exponent.
    """

    e = random.randint(1, 100000000000)
    while not CoprimeTest(phi, e):
        e = random.randint(1, 100000000000)
    return e


def GenerateD(phi, e):
    """
    Selet secret (D) exponent such that it is multiplicatively inverse of e modulo phi (n)

    :param phi: the value of the Euler function
    :param e: open exponent
    :return: secret (D) exponent
    """
    return pow(e, -1, phi)


def keygen():
    """
    Selects a suitable public and private key by the entered prime numbers
    """

    p, q = Generate_prime_number(), Generate_prime_number()
    n = p * q
    phi = Euler(p, q)
    e = GenerateE(phi)
    D = GenerateD(phi, e)

    return n, e, D


def Encode(message):
    """
    Convert the original message into a bit sequence representing the message's symbols as binary numbers 16 bits long

    :param message: original message
    :return: message representing in the bit sequence
    """
    emessage = ""
    for i in message:
        i = ord(i)
        i = '{0:016b}'.format(i)
        emessage += i
    emessage = "1" + emessage
    return emessage

def Encrypt(message):
    """

    Encrypts the input message

    :param message: original message
    :return: encrypted bit sequence
    """
    bitmessage = Encode(message)
    return pow(int(bitmessage), e, n)

def Decode(bitmessage):
    """
    Encodes the input message into a bit sequence

    :param bitmessage: bit sequence of message
    :return: decode message
    """
    bitmessage = bitmessage[1:]
    count = 0
    dmessage = ''
    num = ''
    for i in bitmessage:
        count += 1
        num += i
        if count == 16:
            dmessage += chr(int(num, 2))
            count = 0
            num = ''
    return dmessage

def Decrypt(emessage):
    """
    Gets the bit sequence of the encrypted message ang by calling 'Decode' function gets the decrypted message

    :param emessage: encrypted message
    :return: decrypt message
    """
    bitmessage = str(pow(int(emessage), D, n))
    dmessage = Decode(bitmessage)
    return dmessage

def Creat_electronic_signature(message):
    """
    Returns the digital signature for an input message

    :param message: transmitted message
    :return: digital signature
    """
    signature = Encode(message)
    signature = pow(int(signature), D, n)
    return signature

def Verif_electronic_signature(signature, message):
    """
    Verifies the authenticity of the entered signature

    :param signature: digital signature
    :param message: transmitted message
    :return: result of authenticity's of signature checking
    """
    signature = str(pow(int(signature), e, n))
    message_ = Decode(signature)
    if message_ == message:
        return "Verification successful!"
    else:
        return "Signature is not valid"

def ReadingPrivate(filename):
    """
    Reads private keys from a file
    """
    with open(filename + ".txt", "r") as file:
        n = int(file.readline()[4:])
        D = int(file.readline()[4:])
    return n, D

def RecordingPrivate(n, D, filename):
    """
    Saves private keys to a file
    """
    with open(filename + ".txt", "w") as file:
        file.write("n = " + str(n) + "\n"
                "D = " + str(D) + "\n")

def RecordingPublic(n, e, filename):
    """
    Saves public keys to a file
    """
    with open(filename + ".txt", "w") as file:
        file.write("n = " + str(n) + "\n"
                "e = " + str(e) + "\n")

def ReadingPublic(filename):
    """
    Reads public keys from a file
    """

    with open(filename + ".txt", "r") as file:
        n = int(file.readline()[4:])
        e = int(file.readline()[4:])
    return n, e

if __name__ == '__main__':
    while True:
        order = int(input(
            "Что вы хотите сделать? \nЗашифровать сообщение (1 на клавиатуре),\nРасшифровать (2 на клавиатуре),\nСгенерировать ключи (3 на клавиатуре),\nИспользовать электронную подпись (4 на клавиатуре): \n"))
        if order == 1:
            message = str(input('Введите исходное сообщение М: '))
            order1 = int(input('Какие ключи использовать?\nCобственные ключи (1 на клавиатуре),\nКлючи из файла (2 на клавиатуре): \n'))

            if order1 == 1:
                D = int(input('Введите открытый ключ(e, n):\n' 'e = '))
                n = int(input('n = '))

            if order1 == 2:
                filename = str(input('Введите названия текстового файла для закрытого ключа:\n'))
                n, e = ReadingPublic(filename)
                print('Шифртекст С: ', Encrypt(message))
            else:
                continue

        if order == 2:
            emessage = str(input('Введите шифртекст С: '))
            order1 = int(input('Какие ключи использовать?\nCобственные ключи (1 на клавиатуре),\nКлючи из файла (2 на клавиатуре): \n'))
            if order1 == 1:
                D = int(input('Введите закрытый ключ(D, n):\n' 'D = '))
                n = int(input('n = '))
            if order1 == 2:
                filename = str(input('Введите названия текстового файла для закрытого ключа:\n'))
                n, D = ReadingPrivate(filename)
            print('Исходное сообщение М: ', Decrypt(emessage))
        if order == 3:
            print("Получаю ключи...")
            n, e, D = keygen()
            print('Открытый ключ (e, n): \ne = ', e, '\n'
                                        'n = ', n, '\n'
                                        'Закрытый ключ (D, n): \n'
                                        'D = ', D, '\n'
                                        'n = ', n, '\n'
                  )
            order1 = int(input('Записать ключи в файл?\nДа (1 на клавиатуре)\nНет (2 на клавиатуре)\n'))
            if order1 == 1:
                filename_op = str(input('Введите названия текстового файла для открытого ключа:\n'))
                filename = str(input('Введите названия текстового файла для закрытого ключа:\n'))
                RecordingPublic(n, e, filename)
                RecordingPrivate(n, D, filename)
            else:
                continue

        if order == 4:
            order2 = int(input("Создать подпись (1 на клавитауре)\nПроверить подпись (2 на клавиатуре)? \n"))
            if order2 == 1:
                message = str(input('Введите сообщение М: '))
                order1 = int(input('Какие ключи использовать?\nCобственные ключи (1 на клавиатуре),\nКлючи из файла (2 на клавиатуре): \n'))
                if order1 == 1:
                    D = int(input('Введите закрытый ключ(D, n):\n' 'D = '))
                    n = int(input('n = '))
                if order1 == 2:
                    filename = str(input('Введите названия текстового файла для закрытого ключа:\n'))
                    n, D = ReadingPrivate(filename)
                    print('Ваша электронная подпись S: ', Creat_electronic_signature(message))

            if order2 == 2:
                message = str(input('Введите сообщение М: '))
                signature = str(input('Введите подпись S: '))
                order_key = int(input('Какие ключи использовать?\nCобственные ключи (1 на клавиатуре),\nКлючи из файла (2 на клавиатуре): \n'))
                if order_key == 1:
                    e = int(input('Введите открытый ключ (e, n):\ne = '))
                    n = int(input('n = '))
                if order_key == 2:
                    filename = str(input('Введите названия текстового файла для открытого ключа:\n'))
                    n, e = ReadingPublic(filename)
                print(Verif_electronic_signature(signature, message))
            else:
                continue
        else:
            continue




