from datetime import date
from re import match as re_match

from app.bank_account import BankAccount
from app.smtp_connection import SMTPConnection


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

    @staticmethod
    def __is_promo_code_valid(promo_code: str) -> bool:
        if promo_code is None:
            return False

        pattern = r"^PROM_.{3}$"
        match = re_match(pattern, promo_code)

        return bool(match)

    @staticmethod
    def __is_qualified_for_promo(pesel: str) -> bool:
        if pesel == "Niepoprawny pesel!":
            return False

        year_digits = int(pesel[0:2])
        month_digits = int(pesel[2:4])

        if year_digits > 60 or month_digits > 12:
            return True
        return False

    def take_loan(self, loan_amount: int) -> bool:
        first_condition = self.__check_if_last_three_transfers_are_incoming()
        second_condition = (
            self.__check_if_sum_of_last_five_transfers_is_bigger_than_loan_amount(
                loan_amount
            )
        )

        if first_condition or second_condition:
            self.balance += loan_amount
            return True
        return False

    def __check_if_last_three_transfers_are_incoming(self) -> bool:
        last_three_transfers = self.transfer_history[-3:]
        if len(last_three_transfers) != 3:
            return False
        return all(transfer > 0 for transfer in last_three_transfers)

    def __check_if_sum_of_last_five_transfers_is_bigger_than_loan_amount(
        self, loan_amount: int
    ) -> bool:
        last_five_transfers = self.transfer_history[-5:]
        if len(last_five_transfers) != 5:
            return False
        return sum(last_five_transfers) > loan_amount

    def send_transfer_history_to_mail(
        self, receiver_email: str, smtp_connection: SMTPConnection
    ) -> bool:
        today = date.today()

        subject = f"Wyciąg z dnia {today}"
        content = f"Twoja historia konta to: {self.transfer_history}"

        is_sent_successfully = smtp_connection.send(subject, content, receiver_email)
        return is_sent_successfully
