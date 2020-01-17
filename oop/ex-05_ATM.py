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

# Dodatkowe:
# Zaimplementuj w klasie CashMachine rzucanie wyjątków w następujących przypadkach:
# - brak miejsca na banknoty (ustal limit banknotów w bankomacie)
# - zła wartość wypłacanej sumy (musi być podzielna przez 10)
# - brak odpowiednich banknotów w bankomacie
# Zaimplementuj prosty interfejs tekstowy do klasy bankomat obsługujący wszystkie wyjątki.
# Obsłuż także wyjątki wynikające z podania złych danych przez użytkownika.

class NotEnoughMoney(Exception):
    pass

class NotEnoughPlace(Exception):
    pass

class WrongAmount(Exception):
    pass

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
        if type(amount) == list:
            if len(amount) > 10:
                raise NotEnoughPlace("Wprowadziłeś za dużo banknotów na raz.")
            if sum(amount) % 50 == 0:
                self.bills.extend(amount)
                self.bills.sort()
                self.balance += sum(amount)
            else:
                raise WrongAmount("Zły nominał")
        # if type(amount) == str:
        #     amount = int(amount)
        #     if amount % 50 == 0:
        #         self.balance += amount
        return self.balance, self.bills

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
            raise NotEnoughMoney("Brak środków w bankomacie")


# if __name__ == "__main__":
#     ATM = CashMachine()
#     print("Stan ATM:", ATM.is_available())
#     print("Wpłata 450 zł", ATM.put_money([200, 100, 100, 50]))
#     print("Stan ATM:", ATM.is_available())
#     print("Wpłata 250 zł", ATM.put_money([50, 50, 50, 100]))
#     print("Stan ATM:", ATM.is_available())
#     print("Wypłata 150 zł", ATM.withdraw_money(150))
#     print("Stan ATM:", ATM.is_available())
#     print("Próba wpłaty 60 zł", ATM.put_money([60]))
#     print("Stan ATM:", ATM.is_available())
#     print("Próba wypłaty 60 zł", ATM.withdraw_money(60))
#     print("Stan ATM:", ATM.is_available())
#     print("Wypłata 100 zł", ATM.withdraw_money(100))
#     print("Stan ATM:", ATM.is_available())
#     print("Wypłata 300 zł", ATM.withdraw_money(300))
#     print("Stan ATM:", ATM.is_available())


ATM = CashMachine()
while True:
    operation = input("Włata środków (D) / Wypłata środków (W)")
    if operation == "D":
        ATM.put_money(amount=input("Podaj kwotę:"))
    if operation == "W" and ATM.is_available() == True:
        ATM.withdraw_money(amount=int(input("Podaj kwotę:")))
    else:
        print("Operacja niedostępna.")