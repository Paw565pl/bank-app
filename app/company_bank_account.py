from datetime import date
from os import environ

import requests
from dotenv import load_dotenv

from app.bank_account import BankAccount
from app.smtp_connection import SMTPConnection

load_dotenv()


class CompanyBankAccount(BankAccount):
    express_transfer_fee = 5

    def __init__(self, name: str, nip: str):
        super().__init__()
        self.name = name

        if len(nip) != 10:
            self.nip = "Niepoprawny NIP!"
        else:
            is_nip_in_register = self.__check_if_nip_is_in_register(nip)
            if not is_nip_in_register:
                raise ValueError("given nip is not in the gov register")
            self.nip = nip

    def take_loan(self, loan_amount: int) -> bool:
        first_condition = self.__check_if_balance_is_two_times_higher_than_loan_amount(
            loan_amount
        )
        second_condition = self.__check_if_at_least_one_transfer_to_zus()

        if first_condition and second_condition:
            self.balance += loan_amount
            return True
        return False

    def __check_if_balance_is_two_times_higher_than_loan_amount(
        self, loan_amount: int
    ) -> bool:
        if self.balance >= loan_amount * 2:
            return True
        return False

    def __check_if_at_least_one_transfer_to_zus(self) -> bool:
        if -1775 in self.transfer_history:
            return True
        return False

    @staticmethod
    def __check_if_nip_is_in_register(nip: str) -> bool:
        url = environ.get("BANK_APP_MF_URL")
        today = date.today()
        response = requests.get(f"{url}/{nip}", params={"date": today})

        print(response.status_code)

        if response.status_code == 200:
            return True
        return False

    def send_transfer_history_to_mail(
        self, receiver: str, smtp_connection: SMTPConnection
    ) -> bool:
        today = date.today()

        subject = f"Wyciąg z dnia {today}"
        content = f"Historia konta Twojej firmy to: {self.transfer_history}"

        is_sent_successfully = smtp_connection.send(subject, content, receiver)
        return is_sent_successfully
