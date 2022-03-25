import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_aloitussaldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_saldon_kasvattaminen_toimii(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")

    def test_saldo_vähenee_oikein_maksusta(self):
        self.maksukortti.lataa_rahaa(190)
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti),"saldo: 1.0")

    def test_saldo_liian_pieni(self):
        self.maksukortti.ota_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_rahat_riittävät(self):
        self.assertEqual(self.maksukortti.ota_rahaa(0.05), True)

    def test_rahat_eivät_riitä(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), False)
        