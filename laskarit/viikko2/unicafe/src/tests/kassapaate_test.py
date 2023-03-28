import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = 10000
    
    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kassa), "Kassassa on rahaa 100.00 euroa")      

