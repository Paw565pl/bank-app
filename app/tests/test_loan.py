import unittest

from parameterized import parameterized

from ..CompanyBankAccount import CompanyBankAccount
from ..PrivateBankAccount import PrivateBankAccount


class TestLoan(unittest.TestCase):
    person = {
        "first_name": "Dariusz",
        "last_name": "Januszewski",
        "pesel": "94031633999",
    }

    def setUp(self) -> None:
        self.account = PrivateBankAccount(*self.person.values())

    @parameterized.expand(
        [
            ([], 1000, False, 0),
            ([100, 100, 100], 1000, True, 1000),
            ([-200, 100, 500, 700, -50], 1000, True, 1000),
        ]
    )
    def test_taking_loan(
        self,
        transfer_hsitory: list[int],
        amount: int,
        expected_result: bool,
        expected_balance: int,
    ) -> None:
        self.account.transfer_history = transfer_hsitory
        was_given = self.account.take_loan(amount)
        self.assertEqual(was_given, expected_result)
        self.assertEqual(self.account.balance, expected_balance)
