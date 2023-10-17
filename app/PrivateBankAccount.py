from re import match as re_match
from .BankAccount import BankAccount


class PrivateBankAccount(BankAccount):
    express_transfer_fee = 1

    def __init__(self, first_name, second_name, pesel, promo_code=None):
        self.first_name = first_name
        self.second_name = second_name

        if len(str(pesel)) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

        if self.is_promo_code_valid(promo_code) and self.is_qualified_for_promo(
            self.pesel
        ):
            self.balance = 50

    def is_promo_code_valid(self, promo_code: str) -> bool:
        if promo_code == None:
            return False

        pattern = r"^PROM_.{3}$"
        match = re_match(pattern, promo_code)

        return bool(match)

    def is_qualified_for_promo(self, pesel: str) -> bool:
        if pesel == "Niepoprawny pesel!":
            return False

        year_digits = int(pesel[0:2])
        month_digits = int(pesel[2:4])

        if year_digits > 60 or month_digits > 12:
            return True
        return False
