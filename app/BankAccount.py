from decimal import Decimal


class BankAccount:
    balance = 0
    express_transfer_fee = 0

    def incoming_transfer(self, amount: Decimal) -> None:
        if amount > 0:
            self.balance += amount

    def outgoing_transfer(self, amount: Decimal) -> None:
        if amount > 0 and self.balance >= amount:
            self.balance -= amount

    def express_outgoing_transfer(self, amount: Decimal) -> None:
        if amount > 0 and self.balance >= amount:
            self.balance -= amount + self.express_transfer_fee
