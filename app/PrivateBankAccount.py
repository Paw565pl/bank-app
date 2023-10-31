from re import match as re_match

from .BankAccount import BankAccount


class PrivateBankAccount(BankAccount):
    express_transfer_fee = 1

    def __init__(
        self, first_name: str, last_name: str, pesel: str, promo_code: str | None = None
    ) -> None:
        super().__init__()
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

    def take_loan(self, amount: int) -> bool:
        first_condition = self.__check_if_three_last_transfers_are_incoming()
        second_condition = (
            self.__check_if_sum_of_last_five_transfers_is_bigger_than_loan_amount(
                amount
            )
        )

        if first_condition or second_condition:
            self.balance += amount
            return True

        return False

    def __check_if_three_last_transfers_are_incoming(self) -> bool:
        last_three_transfers = self.transfer_history[-3:]
        if len(last_three_transfers) != 3:
            return False
        return all(transfer > 0 for transfer in last_three_transfers)

    def __check_if_sum_of_last_five_transfers_is_bigger_than_loan_amount(
        self, loan_amount
    ) -> bool:
        last_five_transfers = self.transfer_history[-5:]
        if len(last_five_transfers) != 5:
            return False
        return sum(last_five_transfers) > loan_amount
