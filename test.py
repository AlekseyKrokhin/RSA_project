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

    def test_encrypt(self):
        main.n, main.e, main.D, main.p, main.q = keygen()
        self.assertEqual(Decrypt(Encrypt('Привет')), 'Привет')
        self.assertEqual(Decrypt(Encrypt('Russia is great country')), 'Russia is great country')
        self.assertEqual(Decrypt(Encrypt('2,71828182845904532..,./%')), '2,71828182845904532..,./%')
        self.assertEqual(Decrypt(Encrypt('пи=3,1415==--')), 'пи=3,1415==--')
