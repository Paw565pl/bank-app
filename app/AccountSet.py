from .PrivateBankAccount import PrivateBankAccount


class AccountSet:
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
