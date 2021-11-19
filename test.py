import unittest
import main
from main import GenerateD
from main import Euler
from main import CoprimeTest
from main import Encrypt
from main import Decrypt
from main import keygen
from main import MillerRabin



class UnitTest(unittest.TestCase):

    def test_encrypt(self):
        main.n, main.e, main.D, main.p, main.q = keygen()
        self.assertEqual(Decrypt(Encrypt('Привет')), 'Привет')
        self.assertEqual(Decrypt(Encrypt('Russia is great country')), 'Russia is great country')
        self.assertEqual(Decrypt(Encrypt('2,71828182845904532..,./%')), '2,71828182845904532..,./%')
        self.assertEqual(Decrypt(Encrypt('пи=3,1415==--')), 'пи=3,1415==--')

    def test_D(self):
        self.assertEqual(GenerateD(215, 56), 96)
        self.assertEqual(GenerateD(1111, 16), 625)

    def test_MilerRabin(self):
        self.assertEqual(MillerRabin(17, 5), True)
        self.assertEqual(MillerRabin(2000000, 5), False)
        self.assertEqual(MillerRabin(991447, 5), True)
        self.assertEqual(MillerRabin(512731763812328916, 5), False)
        self.assertEqual(MillerRabin(2989937, 5), True)
        self.assertEqual(MillerRabin(255667864302, 5), False)

    def test_Coprime(self):
        self.assertEqual(CoprimeTest(105, 8), True)
        self.assertEqual(CoprimeTest(2988143, 122346), True)
        self.assertEqual(CoprimeTest(10008, 1066), False)
        self.assertEqual(CoprimeTest(36276516732, 114550), False)





