import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678900"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "Pesel nie został zapisany!")
        self.assertEqual(len(str(pierwsze_konto.pesel)), 11)

    def test_tworzenie_konta_z_krotkim_peselem(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel[::5])
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Pesel nie został zapisany!")

    def test_tworzenie_konta_z_dlugim_peselem(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel + "000")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Pesel nie został zapisany!")

