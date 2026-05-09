class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)

    def _is_valid(self, account: int) -> bool:
        # Accounts are 1-indexed: 1 <= account <= n
        return 1 <= account <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self._is_valid(account1) and self._is_valid(account2):
            # Check if account1 has enough money
            if self.balance[account1 - 1] >= money:
                self.balance[account1 - 1] -= money
                self.balance[account2 - 1] += money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self._is_valid(account):
            self.balance[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self._is_valid(account):
            if self.balance[account - 1] >= money:
                self.balance[account - 1] -= money
                return True
        return False