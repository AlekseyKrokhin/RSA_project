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

    def test_encr(self):
        main.n, main.e, main.D, main.p, main.q = keygen()
        self.assertEqual(Decrypt(Encrypt('Привет')), 'Привет')
        self.assertEqual(Decrypt(Encrypt('AbCdEfАбВгД')), 'AbCdEfАбВгД')
        self.assertEqual(Decrypt(Encrypt('!"№%:,.;@#$%^&*∂å∂ƒ√')), '!"№%:,.;@#$%^&*∂å∂ƒ√')
        self.assertEqual(Decrypt(Encrypt('Фаптш FSF3415__₽')), 'Фаптш FSF3415__₽')
