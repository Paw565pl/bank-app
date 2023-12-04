from datetime import date
from os import environ

import requests
from dotenv import load_dotenv

from .BankAccount import BankAccount

load_dotenv()


class CompanyBankAccount(BankAccount):
    express_transfer_fee = 5

    def __init__(self, company_name: str, nip: str) -> None:
        super().__init__()
        self.company_name = company_name

        if len(nip) != 10:
            self.nip = "Niepoprawny NIP!"
        else:
            is_nip_in_register = self.__check_if_nip_is_in_register(nip)
            if not is_nip_in_register:
                raise ValueError("given nip is not in the gov register")
            self.nip = nip

    def take_loan(self, amount: int) -> bool:
        first_condition = self.__check_if_balance_is_two_times_higher_than_loan_amount(
            amount
        )
        second_condition = self.__check_if_at_least_one_transfer_to_ZUS()

        if first_condition and second_condition:
            self.balance += amount
            return True
        return False

    def __check_if_balance_is_two_times_higher_than_loan_amount(
        self, amount: int
    ) -> bool:
        if self.balance >= amount * 2:
            return True
        return False

    def __check_if_at_least_one_transfer_to_ZUS(self) -> bool:
        if -1775 in self.transfer_history:
            return True
        return False

    def __check_if_nip_is_in_register(self, nip: str) -> bool:
        url = environ.get("BANK_APP_MF_URL")
        today = date.today()
        response = requests.get(f"{url}/{nip}", params={"date": today})

        print(response.status_code)

        if response.status_code == 200:
            return True
        return False
