import unittest

from ..CompanyBankAccount import CompanyBankAccount
from ..PrivateBankAccount import PrivateBankAccount


class TestLoan(unittest.TestCase):
    person = {
        "first_name": "Dariusz",
        "last_name": "Januszewski",
        "pesel": "94031633999",
    }

    def test_loan_private_account_conditions_are_not_met_no_loan(self):
        account = PrivateBankAccount(*self.person.values())
        was_given = account.take_loan(1000)
        self.assertFalse(was_given, "Loan was given!")
        self.assertEqual(account.balance, 0, "Balance was changed!")

    def test_loan_private_account_last_three_transfers_incoming(self):
        account = PrivateBankAccount(*self.person.values())
        account.transfer_history = [100, 100, 100]
        was_given = account.take_loan(1000)
        self.assertTrue(was_given, "Loan was not given!")
        self.assertEqual(account.balance, 1000, "Balance was not changed!")

    def test_loan_private_account_sum_of_transfers(self):
        account = PrivateBankAccount(*self.person.values())
        account.transfer_history = [-200, 100, 500, 700, -50]
        was_given = account.take_loan(1000)
        self.assertTrue(was_given, "Loan was not given!")
        self.assertEqual(account.balance, 1000, "Balance was not changed!")
