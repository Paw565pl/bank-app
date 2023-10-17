import unittest
from ..KontoOsobiste import KontoOsobiste


class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678900"
    za_krotki_pesel = pesel[:5]
    za_dlugi_pesel = pesel + "111"
    kod_promocyjny = "PROM_XYZ"
    niepoprawny_kod_promocyjny = kod_promocyjny[5:]

    def test_tworzenie_konta(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(
            konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!"
        )
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(konto.pesel, self.pesel, "Pesel nie został zapisany!")
        self.assertEqual(len(str(konto.pesel)), 11)

    def test_tworzenie_konta_z_krotkim_peselem(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.za_krotki_pesel)
        self.assertEqual(
            konto.pesel, "Niepoprawny pesel!", "Pesel nie został zapisany!"
        )

    def test_tworzenie_konta_z_dlugim_peselem(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.za_dlugi_pesel)
        self.assertEqual(
            konto.pesel, "Niepoprawny pesel!", "Pesel nie został zapisany!"
        )

    def test_tworzenie_z_poprawnym_kodem_rabatowym(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel, self.kod_promocyjny)
        self.assertEqual(konto.saldo, 50, "Saldo nie zostało zwiększone!")

    def test_tworzenie_z_niepoprawnym_kodem_rabatowym(self):
        konto = KontoOsobiste(
            self.imie, self.nazwisko, self.pesel, self.niepoprawny_kod_promocyjny
        )
        self.assertEqual(konto.saldo, 0, "Saldo zostało zwiększone!")

    def test_tworzenie_z_poprawnym_kodem_rabatowym_zly_pesel(self):
        konto = KontoOsobiste(
            self.imie, self.nazwisko, self.za_krotki_pesel, self.kod_promocyjny
        )
        self.assertEqual(konto.saldo, 0, "Saldo zostało zwiększone!")

    def test_osoba_urodzona_w_1960_brak_zwiekszonego_salda(self):
        konto = KontoOsobiste(
            self.imie, self.nazwisko, "60042687887", self.kod_promocyjny
        )
        self.assertEqual(konto.saldo, 0, "Saldo zostało zwiększone!")

    def test_osoba_urodzona_w_1970_zly_kod_brak_zwiekszonego_salda(self):
        konto = KontoOsobiste(
            self.imie, self.nazwisko, "70092182867", self.niepoprawny_kod_promocyjny
        )
        self.assertEqual(konto.saldo, 0, "Saldo zostało zwiększone!")

    def test_osoba_urodzona_w_1970_zwiekszone_saldo(self):
        konto = KontoOsobiste(
            self.imie, self.nazwisko, "70092182867", self.kod_promocyjny
        )
        self.assertEqual(konto.saldo, 50, "Saldo nie zostało zwiększone!")

    def test_osoba_urodzona_w_2003_zwiekszone_saldo(self):
        konto = KontoOsobiste(
            self.imie, self.nazwisko, "03241178518", self.kod_promocyjny
        )
        self.assertEqual(konto.saldo, 50, "Saldo nie zostało zwiększone!")
