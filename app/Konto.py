class Konto:
    saldo = 0
    express_transfer_fee = 0

    def przelew_wychodzacy(self, kwota):
        if kwota > 0 and self.saldo >= kwota:
            self.saldo -= kwota

    def przelew_przychodzacy(self, kwota):
        if kwota > 0:
            self.saldo += kwota

    def przelew_wychodzacy_ekspresowy(self, kwota):
        if kwota > 0 and self.saldo >= kwota:
            self.saldo -= kwota + self.express_transfer_fee
