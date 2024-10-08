import unittest
from unittest.mock import Mock, patch

from app.bank_account import BankAccount
from app.company_bank_account import CompanyBankAccount
from app.private_bank_account import PrivateBankAccount


class TestTransfersHistory(unittest.TestCase):
    person = {
        "first_name": "Dariusz",
        "last_name": "Januszewski",
        "pesel": "94031633999",
    }
    company = {"name": "test", "nip": "1234567890"}

    def test_standard_transfer(self):
        account = BankAccount()
        account.balance = 100
        account.outgoing_transfer(50)
        account.incoming_transfer(100)
        self.assertEqual(account.transfer_history, [-50, 100])

    def test_private_account_express_transfer(self):
        account = PrivateBankAccount(**self.person)
        account.balance = 100
        account.express_outgoing_transfer(50)
        account.incoming_transfer(100)
        self.assertEqual(
            account.transfer_history, [-50, -account.express_transfer_fee, 100]
        )

    @patch("requests.get")
    def test_company_account_express_transfer(self, check_if_nip_is_in_register: Mock):
        check_if_nip_is_in_register.return_value.status_code = 200
        account = CompanyBankAccount(**self.company)
        account.balance = 100
        account.express_outgoing_transfer(50)
        account.incoming_transfer(100)
        self.assertEqual(
            account.transfer_history, [-50, -account.express_transfer_fee, 100]
        )
