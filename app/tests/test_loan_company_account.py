import unittest
from unittest.mock import Mock, patch

from parameterized import parameterized

from app.company_bank_account import CompanyBankAccount


class TestLoanCompanyAccount(unittest.TestCase):
    company = {"name": "test", "nip": "1234567890"}

    @patch("requests.get")
    def setUp(self, check_if_nip_is_in_register: Mock) -> None:
        check_if_nip_is_in_register.return_value.status_code = 200
        self.account = CompanyBankAccount(**self.company)

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
