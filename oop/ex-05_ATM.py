class CashMachine:
    def __init__(self):
        self.balance = 0
        self.bill = []

    def is_available(self):
        if self.balance > 50:
            return True
        else:
            return False

    def put_money(self, money):
        if money % 50 == 0:
            self.bill.append(money)
            (self.bill).sort()
            self.balance += money
            return self.balance, self.bill
        else:
            return "Zły nominał"

    def withdraw_money(self, money):
        if money % 50 == 0 and money <= self.balance:
            self.balance -= money
            col_money = money
            for i in self.bill:
                if i == money:
                    (self.bill).remove(i)
                if i < money:
                    col_money -= 50
                    (self.bill).remove(col_money)
                if i > min(self.bill): #or i < max(self.bill):
                    return "Brak środków w bankomacie"
            return self.balance, self.bill
        elif money % 50 == 0 and money > self.balance:
            return "Brak środków w bankomacie"
        else:
            return "Zły nominał"


if __name__ == "__main__":
    ATM = CashMachine()
    print(ATM.is_available())
    print(ATM.put_money(200))
    print(ATM.put_money(100))
    print(ATM.put_money(100))
    print(ATM.put_money(50))
    print(ATM.is_available())
    print(ATM.withdraw_money(150))
    print(ATM.is_available())
    print(ATM.put_money(60))
    print(ATM.is_available())
    print(ATM.withdraw_money(100))
    print(ATM.is_available())
    print(ATM.withdraw_money(50))