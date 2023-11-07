from .PrivateBankAccount import PrivateBankAccount


class AccountSet:
    personal_accounts = []

    @classmethod
    def add_personal_account(cls, account: PrivateBankAccount) -> None:
        cls.personal_accounts.append(account)

    @classmethod
    def get_personal_accounts_count(cls):
        return len(cls.personal_accounts)

    @classmethod
    def get_personal_account_by_pesel(cls, pesel: str) -> PrivateBankAccount | None:
        found_account = [
            account for account in cls.personal_accounts if account.pesel == pesel
        ]

        if len(found_account) != 0:
            return found_account[0]
        return None
