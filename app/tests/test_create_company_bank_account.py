import unittest
from unittest.mock import Mock, patch

from ..CompanyBankAccount import CompanyBankAccount


@patch(
    "app.CompanyBankAccount.CompanyBankAccount._CompanyBankAccount__check_if_nip_is_in_register"
)
class TestCreateCompanyBankAccount(unittest.TestCase):
    company_name = "test company"
    nip = "8461627563"
    invalid_nip = "1234567891"

    def test_valid_data(self, check_if_nip_is_in_register: Mock):
        check_if_nip_is_in_register.return_value = True
        account = CompanyBankAccount(self.company_name, self.nip)
        self.assertEqual(
            account.company_name, self.company_name, "Invalid company name!"
        )
        self.assertEqual(account.nip, self.nip, "Bad nip!")

    def test_invalid_nip(self, _):
        account = CompanyBankAccount(self.company_name, "")
        self.assertEqual(account.nip, "Niepoprawny NIP!", "Nip was saved!")

    def test_nip_not_in_gov_register(self, check_if_nip_is_in_register: Mock):
        check_if_nip_is_in_register.return_value = False
        with self.assertRaises(ValueError) as context:
            CompanyBankAccount(self.company_name, self.invalid_nip)
        self.assertTrue(
            "given nip is not in the gov register" in str(context.exception)
        )
