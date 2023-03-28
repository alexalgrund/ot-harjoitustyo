import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_asettaa_saldon_oikein(self):
        # alustetaan maksukortti, jossa on 10 euroa (1000 senttiä)
        kortti = Maksukortti(1000)
        vastaus = str(kortti)
        self.assertEqual(vastaus, "Kortilla on rahaa 10.00 euroa")

    def test_lataa_rahan_oikein(self):
        self.kortti.lataa_rahaa(2500)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35.00 euroa")
    
    def test_vahentaa_saldon_oikein(self):
        self.kortti.ota_rahaa(500)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 5.00 euroa")
    
    def test_rahaa_on_liian_vahan(self):
        self.kortti.ota_rahaa(2000)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")







