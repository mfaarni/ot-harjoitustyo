import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti=Maksukortti(1000)


    def test_alkurahat(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_alkulounaat(self):
        self.assertEqual(self.kassapaate.edulliset+self.kassapaate.maukkaat, 0)

    def test_käteisellä_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500),260)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100240)

    def test_kateisella_edullinen_ei_varaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(1),1)


    def test_käteisellä_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(1000),600)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100400)

    def test_käteisellä_edullinen_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_käteisellä_maukas_maara(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.maukkaat,1)
    
    def test_kateisella_maksu_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(1.3),1.3)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    #MAKSUKORTIN TESTIT


    def test_kortilla_tarpeeksi_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100),True)

    def test_kortilla_lounas(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset,1)
        self.assertEqual(self.kassapaate.maukkaat,1)
 
    
    def test_kortilla_ei_tarpeeksi_rahaa_edullinen(self):
        self.maksukortti.ota_rahaa(999)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),False)
        self.assertEqual(self.maksukortti.saldo,1)

    
    def test_kortilla_ei_tarpeeksi_rahaa_maukas(self):
        self.maksukortti.ota_rahaa(999)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),False)
        self.assertEqual(self.maksukortti.saldo,1)

    def test_kassa_ei_muutu_korttiostoksesta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
    
    def test_kortille_ladataan_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,1000)
        self.assertEqual(self.maksukortti.saldo,2000)
        self.assertEqual(self.kassapaate.kassassa_rahaa,101000)

    def test_ladataan_rahaa_neg(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-100)
        self.assertEqual(self.maksukortti.saldo,1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)