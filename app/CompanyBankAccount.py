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
