import unittest
from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678900"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(
            pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!"
        )
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "Pesel nie został zapisany!")
        self.assertEqual(len(str(pierwsze_konto.pesel)), 11)

    def test_tworzenie_konta_z_krotkim_peselem(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel[:5])
        self.assertEqual(
            konto.pesel, "Niepoprawny pesel!", "Pesel nie został zapisany!"
        )

    def test_tworzenie_konta_z_dlugim_peselem(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel + "000")
        self.assertEqual(
            konto.pesel, "Niepoprawny pesel!", "Pesel nie został zapisany!"
        )

    def test_tworzenie_z_poprawnym_kodem_rabatowym(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PROM_XYZ")
        self.assertEqual(konto.saldo, 50, "Saldo nie zostało zwiększone!")

    def test_tworzenie_z_niepoprawnym_kodem_rabatowym(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "XYZ1")
        self.assertEqual(konto.saldo, 0, "Saldo zostało zwiększone!")

    def test_zly_pesel_brak_zwiekszonego_salda(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel[:5], "PROM_XYZ")
        self.assertEqual(konto.saldo, 0, "Saldo zostało zwiększone!")

    def test_osoba_urodzona_w_1960_brak_zwiekszonego_salda(self):
        konto = Konto(self.imie, self.nazwisko, "60042687887", "PROM_XYZ")
        self.assertEqual(konto.saldo, 0, "Saldo zostało zwiększone!")

    def test_osoba_urodzona_w_1970_zly_kod_brak_zwiekszonego_salda(self):
        konto = Konto(self.imie, self.nazwisko, "70092182867", "XYZ1")
        self.assertEqual(konto.saldo, 0, "Saldo zostało zwiększone!")

    def test_osoba_urodzona_w_1970_zwiekszone_saldo(self):
        konto = Konto(self.imie, self.nazwisko, "70092182867", "PROM_XYZ")
        self.assertEqual(konto.saldo, 50, "Saldo nie zostało zwiększone!")

    def test_osoba_urodzona_w_2003_zwiekszone_saldo(self):
        konto = Konto(self.imie, self.nazwisko, "03241178518", "PROM_XYZ")
        self.assertEqual(konto.saldo, 50, "Saldo nie zostało zwiększone!")
