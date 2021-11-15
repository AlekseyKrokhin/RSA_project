import unittest
import main
from main import CoprimeTest
from main import GenerateD_e
from main import Encrypt
from main import Decrypt
from main import keygen
from main import MillerRabin
from main import Generate_prime_number


class UnitTest(unittest.TestCase):

    def test_coprime(self):
        self.assertEqual(CoprimeTest(13, 3), True)
        self.assertEqual(CoprimeTest(15, 5), False)
        self.assertEqual(CoprimeTest(92, 4), False)
        self.assertEqual(CoprimeTest(17, 3), True)

    def test_D(self):
        self.assertEqual(GenerateD_e(5, 192), 77)
        self.assertEqual(GenerateD_e(17, 231), 68)
        self.assertEqual(GenerateD_e(491, 979), 327)

    def test_encr(self):
        main.n, main.e, main.D, main.p, main.q = keygen()
        self.assertEqual(Decrypt(Encrypt('Привет')), 'Привет')
        self.assertEqual(Decrypt(Encrypt('AbCdEfАбВгД')), 'AbCdEfАбВгД')
        self.assertEqual(Decrypt(Encrypt('!"№%:,.;@#$%^&*∂å∂ƒ√')), '!"№%:,.;@#$%^&*∂å∂ƒ√')
        self.assertEqual(Decrypt(Encrypt('Фаптш FSF3415__₽')), 'Фаптш FSF3415__₽')

    def test_isprime(self):
        self.assertEqual(isPrime(77), False)
        self.assertEqual(isPrime(7), True)
        self.assertEqual(isPrime(15), False)
        self.assertEqual(isPrime(881), True)
        self.assertEqual(isPrime(1000000), False)
        self.assertEqual(isPrime(2), True)
        self.assertEqual(isPrime(1), False)
        self.assertEqual(isPrime(999983), True)