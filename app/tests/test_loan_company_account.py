import unittest

from parameterized import parameterized

from ..CompanyBankAccount import CompanyBankAccount


class TestLoanCompanyAccount(unittest.TestCase):
    company = {"name": "test", "nip": "1234567890"}

    def setUp(self) -> None:
        self.account = CompanyBankAccount(*self.company.values())

    @parameterized.expand(
        [
            ([], 100, 1000, False, 100),
            ([-1775], 2000, 1000, True, 3000),
            ([-1775], 500, 1000, False, 500),
        ]
    )
    def test_taking_loan(
        self,
        transfer_hsitory: list[int],
        balance: int,
        amount: int,
        expected_result: bool,
        expected_balance: int,
    ) -> None:
        self.account.transfer_history = transfer_hsitory
        self.account.balance = balance
        was_given = self.account.take_loan(amount)
        self.assertEqual(was_given, expected_result)
        self.assertEqual(self.account.balance, expected_balance)
