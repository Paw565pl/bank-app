import unittest

from app import KontoFirmowe
from ..KontoOsobiste import KontoOsobiste


class TestBankAccountTransfers(unittest.TestCase):
    osoba1 = {"imie1": "Dariusz", "nazwisko1": "Januszewski", "pesel1": "94031633999"}

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

    def test_express_transfer_private_account(self):
        konto = KontoOsobiste(*self.osoba1.values())
        konto.saldo = 120
        konto.przelew_wychodzacy_ekspresowy(100)
        self.assertEqual(konto.saldo, 120 - 100 - 1, "Saldo nie jest poprawne!")

    def test_express_transfer_company_account(self):
        konto = KontoFirmowe("test1", "1234567890")
        konto.saldo = 120
        konto.przelew_wychodzacy_ekspresowy(100)
        self.assertEqual(konto.saldo, 120 - 100 - 5, "Saldo nie jest poprawne!")

    def test_express_transfer_with_amount_greater_than_balance(self):
        konto = KontoOsobiste(*self.osoba1.values())
        konto.saldo = 200
        konto.przelew_wychodzacy_ekspresowy(300)
        self.assertEqual(konto.saldo, 200, "Saldo nie jest poprawne!")
