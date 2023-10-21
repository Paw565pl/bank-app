from re import match as re_match
from .BankAccount import BankAccount


class PrivateBankAccount(BankAccount):
    express_transfer_fee = 1

    def __init__(
        self, first_name: str, last_name: str, pesel: str, promo_code: str | None = None
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name

        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

        if self.__is_promo_code_valid(promo_code) and self.__is_qualified_for_promo(
            self.pesel
        ):
            self.balance = 50

    def __is_promo_code_valid(self, promo_code: str) -> bool:
        if promo_code is None:
            return False

        pattern = r"^PROM_.{3}$"
        match = re_match(pattern, promo_code)

        return bool(match)

    def __is_qualified_for_promo(self, pesel: str) -> bool:
        if pesel == "Niepoprawny pesel!":
            return False

        year_digits = int(pesel[0:2])
        month_digits = int(pesel[2:4])

        if year_digits > 60 or month_digits > 12:
            return True
        return False
