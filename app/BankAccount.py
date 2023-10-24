class BankAccount:
    express_transfer_fee = 0

    def __init__(self):
        self.balance = 0
        self.transfer_history = []

    def incoming_transfer(self, amount: int) -> None:
        if amount > 0:
            self.balance += amount
            self.transfer_history.append(amount)

    def outgoing_transfer(self, amount: int) -> None:
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transfer_history.append(-amount)

    def express_outgoing_transfer(self, amount: int) -> None:
        if amount > 0 and self.balance >= amount:
            self.balance -= amount + self.express_transfer_fee
            self.transfer_history.append(-amount)
            self.transfer_history.append(-self.express_transfer_fee)
