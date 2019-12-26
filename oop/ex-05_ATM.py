# Zaimplementuj klase CashMachine umozliwiajaca wpłacanie i
# wypłacanie pieniedzy. Zadbaj o to aby stan bankomatu
# przetrzymywany był w zmiennych prywatnych.
# Przykład uzycia:
# >>> cash_machine = CashMachine()
# >>> cash_machine.is_available()
# False
# >>> cash_machine.put_money([200, 100, 100, 50])
# >>> cash_machine.is_available()
# True
# >>> cash_machine.withdraw_money(150)
# [100, 50]


class CashMachine:
    def __init__(self):
        self.bills = []
        self.balance = 0

    def is_available(self):
        if self.balance >= 50 and self.balance == sum(self.bills):
            return True
        else:
            return False

    def put_money(self, amount):
        if sum(amount) % 50 == 0:
            self.bills.extend(amount)
            self.bills.sort()
            self.balance += sum(amount)
            return self.balance, self.bills
        else:
            return "Zły nominał"

    def withdraw_money(self, amount):
        collected_bills = []
        collected_sum = 0
        self.bills.sort(reverse=True)
        for bill in self.bills:
            if bill + collected_sum <= amount:
                collected_sum += bill
                collected_bills.append(bill)
        if collected_sum == amount:
            self.balance -= collected_sum
            for bill in collected_bills:
                self.bills.remove(bill)
            return self.balance, self.bills
        else:
            return "Brak środków w bankomacie"


if __name__ == "__main__":
    ATM = CashMachine()
    print("Stan ATM:", ATM.is_available())
    print("Wpłata 450 zł", ATM.put_money([200, 100, 100, 50]))
    print("Stan ATM:", ATM.is_available())
    print("Wpłata 250 zł", ATM.put_money([50, 50, 50, 100]))
    print("Stan ATM:", ATM.is_available())
    print("Wypłata 150 zł", ATM.withdraw_money(150))
    print("Stan ATM:", ATM.is_available())
    print("Próba wpłaty 60 zł", ATM.put_money([60]))
    print("Stan ATM:", ATM.is_available())
    print("Próba wypłaty 60 zł", ATM.withdraw_money(60))
    print("Stan ATM:", ATM.is_available())
    print("Wypłata 100 zł", ATM.withdraw_money(100))
    print("Stan ATM:", ATM.is_available())
    print("Wypłata 300 zł", ATM.withdraw_money(300))
    print("Stan ATM:", ATM.is_available())