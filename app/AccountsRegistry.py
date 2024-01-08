import copy

from pymongo import MongoClient

from app.PrivateBankAccount import PrivateBankAccount


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
    def save(self) -> int:
        self.collection.drop()

        private_accounts_dicts = [
            copy.deepcopy(account.__dict__) for account in self.private_accounts
        ]
        self.collection.insert_many(private_accounts_dicts)

        return self.collection.count_documents({})

    @classmethod
    def load(self) -> int:
        self.private_accounts = []

        db_accounts = self.collection.find()

        private_accounts_objs = []
        for account in db_accounts:
            account_obj = PrivateBankAccount(
                account["first_name"], account["last_name"], account["pesel"]
            )
            account_obj.balance = account["balance"]
            account_obj.transfer_history = account["transfer_history"]
            private_accounts_objs.append(account_obj)

        self.private_accounts = private_accounts_objs

        return self.collection.count_documents({})
