from decimal import Decimal
class Account:
    def __init__(self,name:str, balance:Decimal):
        self.__name = name
        if balance < Decimal(0):
            raise ValueError("balance cannot be less than 0")
        self.__balance = balance

    def deposit(self,amount):
        if amount <= Decimal(0.00):
            raise  ValueError("amount cannot be less than zero")
        self.balance += amount
a1 = Account("praise", Decimal(-500))
