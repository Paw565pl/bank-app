import unittest
from unittest.mock import Mock, patch

from app.AccountSet import AccountSet
from app.PrivateBankAccount import PrivateBankAccount


class TestAccountsSet(unittest.TestCase):
    person = {
        "first_name": "Dariusz",
        "last_name": "Januszewski",
        "pesel": "94031633999",
    }

    @classmethod
    def setUpClass(cls) -> None:
        cls.account = PrivateBankAccount(*cls.person.values())
        AccountSet.add_private_account(cls.account)

    @classmethod
    def tearDownClass(cls) -> None:
        AccountSet.private_accounts = []

    def test_add(self):
        new_account = PrivateBankAccount(*self.person.values())
        AccountSet.add_private_account(new_account)
        self.assertEqual(
            AccountSet.private_accounts,
            [self.account, new_account],
            "Account was not added!",
        )

    def test_count(self):
        count = AccountSet.get_private_accounts_count()
        self.assertEqual(count, 2, "Wrong count was returned!")

    def test_find_by_pesel_account_does_not_exists(self):
        found_account = AccountSet.get_private_account_by_pesel("11111111111")
        self.assertEqual(found_account, None, "Account was found!")

    def test_find_by_pesel_account_exists(self):
        found_account = AccountSet.get_private_account_by_pesel(self.person["pesel"])
        self.assertEqual(found_account, self.account, "Wrong account was found!")

    @patch("app.AccountSet.AccountSet.collection")
    def test_save_accounts_to_db(self, collection_mock: Mock):
        private_accounts_dicts = [
            account.__dict__ for account in AccountSet.private_accounts
        ]

        AccountSet.save()

        collection_mock.drop.assert_called_once()
        collection_mock.insert_many.assert_called_once_with(private_accounts_dicts)

    @patch("app.AccountSet.AccountSet.collection")
    def test_load_accounts_from_db(self, collection_mock: Mock):
        private_accounts = AccountSet.private_accounts
        private_accounts_dicts = [
            account.__dict__ for account in AccountSet.private_accounts
        ]
        collection_mock.find.return_value = private_accounts_dicts

        AccountSet.load()

        self.assertEqual(
            len(AccountSet.private_accounts),
            len(private_accounts),
            "Invalid number of accounts!",
        )
        self.assertEqual(
            AccountSet.private_accounts[0].__dict__,
            private_accounts[0].__dict__,
            "Invalid account data!",
        )
        self.assertEqual(
            AccountSet.private_accounts[1].__dict__,
            private_accounts[1].__dict__,
            "Invalid account data!",
        )
