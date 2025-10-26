class Bank:

    def __init__(self, balance: List[int]):
        self.balances = [b for b in balance]
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (0 < account1 <= len(self.balances)) or self.balances[account1 - 1] < money:
            return False
        if not (0 < account2 <= len(self.balances)):
            return False
        
        self.withdraw(account1, money)
        self.deposit(account2, money)
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not (0 < account <= len(self.balances)):
            return False
        
        self.balances[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not (0 < account <= len(self.balances)) or self.balances[account - 1] < money:
            return False
        
        self.balances[account - 1] -= money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)