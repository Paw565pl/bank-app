class Konto:
    def przelew_wychodzacy(self, kwota):
        if kwota > 0 and self.saldo >= kwota:
            self.saldo -= kwota

    def przelew_przychodzacy(self, kwota):
        if kwota > 0:
            self.saldo += kwota
