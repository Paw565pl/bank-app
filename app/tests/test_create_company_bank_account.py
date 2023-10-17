import unittest
from ..KontoFirmowe import KontoFirmowe


class TestCreateCompanyBankAccount(unittest.TestCase):
    company_name = "test company"
    good_nip = "1234567890"

    def test_create_good_data(self):
        konto = KontoFirmowe(self.company_name, self.good_nip)
        self.assertEqual(konto.company_name, self.company_name, "Bad company name!")
        self.assertEqual(konto.nip, self.good_nip, "Bad nip!")

    def test_create_bad_data(self):
        konto = KontoFirmowe(self.company_name, "")
        self.assertEqual(konto.company_name, self.company_name, "Bad company name!")
        self.assertEqual(konto.nip, "Niepoprawny NIP!", "Nip was saved!")
