import unittest
from ..KontoOsobiste import KontoOsobiste


class TestBankAccountTransfers(unittest.TestCase):
    osoba1 = {"imie1": "Dariusz", "nazwisko1": "Januszewski", "pesel1": "94031633999"}
    # osoba2 = {"imie2": "Janusz", "nazwisko2": "Dariuszewski", "pesel2": "94031637672"}

    def test_przelew_wychodzacy_brak_salda_brak_zmiany_salda(self):
        konto = KontoOsobiste(*self.osoba1.values())
        konto.przelew_wychodzacy(50)
        self.assertEqual(konto.saldo, 0, "Saldo zmieniło się!")

    def test_przelew_wychodzacy_jest_saldo_zmiana_salda(self):
        konto = KontoOsobiste(*self.osoba1.values())
        konto.saldo = 100
        konto.przelew_wychodzacy(50)
        self.assertEqual(konto.saldo, 50, "Saldo nie zmniejszyło się!")

    def test_przelew_przychodzacy_zmiana_salda(self):
        konto = KontoOsobiste(*self.osoba1.values())
        konto.przelew_przychodzacy(50)
        self.assertEqual(konto.saldo, 50, "Saldo nie zwiększyło się!")
