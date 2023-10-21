import unittest
from ..BankAccount import BankAccount
from ..PrivateBankAccount import PrivateBankAccount
from ..CompanyBankAccount import CompanyBankAccount


class TestBankAccountTransfers(unittest.TestCase):
    person = {
        "first_name": "Dariusz",
        "last_name": "Januszewski",
        "pesel": "94031633999",
    }
    company = {"name": "test", "nip": "1234567890"}

    def test_incoming_transfer_balance_change(self):
        account = BankAccount()
        account.incoming_transfer(50)
        self.assertEqual(account.balance, 50, "Balance was not increased!")

    def test_outgoing_transfer_too_low_balance_no_balance_change(self):
        account = BankAccount()
        account.outgoing_transfer(50)
        self.assertEqual(account.balance, 0, "Balance was changed!")

    def test_outgoing_transfer_balance_change(self):
        account = BankAccount()
        account.balance = 100
        account.outgoing_transfer(50)
        self.assertEqual(account.balance, 50, "Balance was not decreased!")

    def test_express_transfer_private_account(self):
        account = PrivateBankAccount(*self.person.values())
        account.balance = 200
        account.express_outgoing_transfer(100)
        self.assertEqual(account.balance, 200 - 100 - 1, "Balance is invalid!")

    def test_express_transfer_company_account(self):
        account = CompanyBankAccount(*self.company.values())
        account.balance = 200
        account.express_outgoing_transfer(100)
        self.assertEqual(account.balance, 200 - 100 - 5, "Balance is invalid!")

    def test_express_transfer_amount_greater_than_balance(self):
        account = PrivateBankAccount(*self.person.values())
        account.balance = 200
        account.express_outgoing_transfer(300)
        self.assertEqual(account.balance, 200, "Balance was changed!")
