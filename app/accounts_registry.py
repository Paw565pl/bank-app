from copy import deepcopy

from pymongo import MongoClient

from app.private_bank_account import PrivateBankAccount


class AccountsRegistry:
    client = MongoClient("localhost", 27017)
    db = client["bank_app_db"]
    collection = db["accounts_registry"]

    private_accounts = []

    @classmethod
    def add_private_account(cls, account: PrivateBankAccount) -> None:
        cls.private_accounts.append(account)

    @classmethod
    def get_private_accounts_count(cls):
        return len(cls.private_accounts)

    @classmethod
    def get_private_account_by_pesel(cls, pesel: str) -> PrivateBankAccount | None:
        found_account = [
            account for account in cls.private_accounts if account.pesel == pesel
        ]

        if len(found_account) != 0:
            return found_account[0]
        return None

    @classmethod
    def save(cls) -> int:
        cls.collection.drop()

        private_accounts_dicts = [
            deepcopy(account.__dict__) for account in cls.private_accounts
        ]
        cls.collection.insert_many(private_accounts_dicts)

        return cls.collection.count_documents({})

    @classmethod
    def load(cls) -> int:
        cls.private_accounts = []

        db_accounts = cls.collection.find()

        private_accounts_objs = []
        for account in db_accounts:
            account_obj = PrivateBankAccount(
                account["first_name"], account["last_name"], account["pesel"]
            )
            account_obj.balance = account["balance"]
            account_obj.transfer_history = account["transfer_history"]
            private_accounts_objs.append(account_obj)

        cls.private_accounts = private_accounts_objs

        return cls.collection.count_documents({})
