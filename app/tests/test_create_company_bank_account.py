import unittest
from ..CompanyBankAccount import CompanyBankAccount


class TestCreateCompanyBankAccount(unittest.TestCase):
    company_name = "test company"
    nip = "1234567890"

    def test_valid_data(self):
        account = CompanyBankAccount(self.company_name, self.nip)
        self.assertEqual(
            account.company_name, self.company_name, "Invalid company name!"
        )
        self.assertEqual(account.nip, self.nip, "Bad nip!")

    def test_invalid_nip(self):
        account = CompanyBankAccount(self.company_name, "")
        self.assertEqual(account.nip, "Niepoprawny NIP!", "Nip was saved!")
