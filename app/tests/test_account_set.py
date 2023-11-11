import unittest

from ..AccountSet import AccountSet
from ..PrivateBankAccount import PrivateBankAccount


class TestAccountsSet(unittest.TestCase):
    person = {
        "first_name": "Dariusz",
        "last_name": "Januszewski",
        "pesel": "94031633999",
    }

    @classmethod
    def setUp(cls) -> None:
        cls.account = PrivateBankAccount(*cls.person.values())
        AccountSet.add_personal_account(cls.account)

    @classmethod
    def tearDown(cls) -> None:
        AccountSet.personal_accounts = []

    def test_add(self):
        new_account = PrivateBankAccount(*self.person.values())
        AccountSet.add_personal_account(new_account)
        self.assertEqual(
            AccountSet.personal_accounts,
            [self.account, new_account],
            "Account was not added!",
        )

    def test_count(self):
        count = AccountSet.get_personal_accounts_count()
        self.assertEqual(count, 1, "Wrong count was returned!")

    def test_find_by_pesel_account_does_not_exists(self):
        found_account = AccountSet.get_personal_account_by_pesel("11111111111")
        self.assertEqual(found_account, None, "Account was found!")

    def test_find_by_pesel_account_exists(self):
        found_account = AccountSet.get_personal_account_by_pesel(self.person["pesel"])
        self.assertEqual(found_account, self.account, "Wrong account was found!")
