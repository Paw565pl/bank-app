from .BankAccount import BankAccount


class CompanyBankAccount(BankAccount):
    express_transfer_fee = 5

    def __init__(self, company_name: str, nip: str) -> None:
        super().__init__()
        self.company_name = company_name

        if len(nip) == 10:
            self.nip = nip
        else:
            self.nip = "Niepoprawny NIP!"

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

    def __check_if_at_least_one_transfer_to_ZUS(self):
        if -1775 in self.transfer_history:
            return True
        return False
