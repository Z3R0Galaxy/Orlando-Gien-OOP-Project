class UserAccount:
    def __init__(self, username, bank_number, balance=0.0):
        self.username = username
        self.bank_number = bank_number
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def to_dict(self):
        return {
            'username': self.username,
            'bank_number': str(self.bank_number),
            'balance': str(self.balance)
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            username=data['username'],
            bank_number=int(data['bank_number']),
            balance=float(data['balance'])
        )