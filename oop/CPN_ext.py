# Wersja rozszerzona - zadanie dodatkowe:
# podczas tankowania użytkownik może podać (opcjonalnie) numer rejestracyjny samochodu. Dla użytkowników podających swój
# numer, którzy zatankowali w sumie ponad 1000 l, przyznaj rabat w wysokości 0.10 PLN na każdym litrze.

class Gas_Station:
    def __init__(self):
        self.E95_supply = 0
        self.E98_supply = 0
        self.ON_supply = 0
        self.ON_premium_supply = 0
        self.E95_price = 0
        self.E98_price = 0
        self.ON_price = 0
        self.ON_premium_price = 0
        self.loyality_club = {}
        self.gas_buy = 0
        self.gas_sell = 0

    def gas_station_pumping_and_balance(self, type_of_fuel, amount, price):
        if type_of_fuel == "E95":
            if self.E95_supply + amount > 2500:
                self.E95_supply += 2500 - self.E95_supply
                self.gas_buy += amount * price
            else:
                self.E95_supply += amount
                self.gas_buy += amount * price
        if type_of_fuel == "E98":
            if self.E98_supply + amount > 2500:
                self.E98_supply += 2500 - self.E98_supply
                self.gas_buy += amount * price
            else:
                self.E98_supply += amount
                self.gas_buy += amount * price
        if type_of_fuel == "ON":
            if self.ON_supply + amount > 2500:
                self.ON_supply += 2500 - self.ON_supply
                self.gas_buy += amount * price
            else:
                self.ON_supply += amount
                self.gas_buy += amount * price
        if type_of_fuel == "ON_premium":
            if self.ON_premium_supply + amount > 2500:
                self.ON_premium_supply += 2500 - self.ON_premium_supply
                self.gas_buy += amount * price
            else:
                self.ON_premium_supply += amount
                self.gas_buy += amount * price
        return f"""Stan poszczególnych paliw:
\t- E95 - {self.E95_supply} litrów;
\t- E98 - {self.E98_supply} litrów;
\t- ON - {self.ON_supply} litrów;
\t- ON premium - {self.ON_premium_supply} litrów."""

    def gas_price_car(self, type_of_fuel, price):
        if type_of_fuel == "E95":
            self.E95_price = price
        if type_of_fuel == "E98":
            self.E98_price = price
        if type_of_fuel == "ON":
            self.ON_price = price
        if type_of_fuel == "ON_premium":
            self.ON_premium_price = price

    def car_refuelling(self, type_of_fuel, amount, plate):
        if type_of_fuel == "E95" and self.E95_price != 0:
            if amount <= self.E95_supply:
                self.E95_supply -= amount
            else:
                amount = self.E95_supply
                self.E95_supply -= amount
            if plate == "Brak":
                self.loyality_club["Brak"] = 0
                self.gas_sell += amount * self.E95_price
                car_sell = amount * self.E95_price
            elif plate not in self.loyality_club:
                self.loyality_club[plate] = amount
                self.gas_sell += amount * self.E95_price
                car_sell = amount * self.E95_price
            else:
                self.loyality_club[plate] += amount
                if self.loyality_club[plate] >= 1000:
                    self.gas_sell += amount * self.E95_price
                    car_sell = amount * (self.E95_price - 0.10)
                else:
                    self.gas_sell += amount * self.E95_price
                    car_sell = amount * self.E95_price
            print(f"Zatankowałeś {amount}l. E95 za {car_sell:.2f} zł. Stan karty lojalnościowej: {self.loyality_club[plate]}")
        if type_of_fuel == "E98" and self.E98_price != 0:
            if amount <= self.E98_supply:
                self.E98_supply -= amount
            else:
                amount = self.E98_supply
                self.E98_supply -= amount
            if plate == "Brak":
                self.loyality_club["Brak"] = 0
                self.gas_sell += amount * self.E98_price
                car_sell = amount * self.E98_price
            elif plate not in self.loyality_club:
                self.loyality_club[plate] = amount
                self.gas_sell += amount * self.E98_price
                car_sell = amount * self.E98_price
            else:
                self.loyality_club[plate] += amount
                if self.loyality_club[plate] >= 1000:
                    self.gas_sell += amount * self.E98_price
                    car_sell = amount * (self.E98_price - 0.10)
                else:
                    self.gas_sell += amount * self.E98_price
                    car_sell = amount * self.E98_price
            print(f"Zatankowałeś {amount}l. E98 za {car_sell:.2f} zł. Stan karty lojalnościowej: {self.loyality_club[plate]}")
        if type_of_fuel == "ON" and self.ON_price != 0:
            if amount <= self.ON_supply:
                self.ON_supply -= amount
            else:
                amount = self.ON_supply
                self.ON_supply -= amount
            if plate == "Brak":
                self.loyality_club["Brak"] = 0
                self.gas_sell += amount * self.ON_price
                car_sell = amount * self.ON_price
            elif plate not in self.loyality_club:
                self.loyality_club[plate] = amount
                self.gas_sell += amount * self.ON_price
                car_sell = amount * self.ON_price
            else:
                self.loyality_club[plate] += amount
                if self.loyality_club[plate] >= 1000:
                    self.gas_sell += amount * self.ON_price
                    car_sell = amount * (self.ON_price - 0.10)
                else:
                    self.gas_sell += amount * self.ON_price
                    car_sell = amount * self.ON_price
            print(f"Zatankowałeś {amount}l. ON za {car_sell:.2f} zł. Stan karty lojalnościowej: {self.loyality_club[plate]}")
        if type_of_fuel == "ON_premium" and self.ON_premium_price != 0:
            if amount <= self.ON_premium_supply:
                self.ON_premium_supply -= amount
            else:
                amount = self.ON_premium_supply
                self.ON_premium_supply -= amount
            if plate == "Brak":
                self.loyality_club["Brak"] = 0
                self.gas_sell += amount * self.ON_premium_price
                car_sell = amount * self.ON_premium_price
            elif plate not in self.loyality_club:
                self.loyality_club[plate] = amount
                self.gas_sell += amount * self.ON_premium_price
                car_sell = amount * self.ON_premium_price
            else:
                self.loyality_club[plate] += amount
                if self.loyality_club[plate] >= 1000:
                    self.gas_sell += amount * self.ON_premium_price
                    car_sell = amount * (self.ON_premium_price - 0.10)
                else:
                    self.gas_sell += amount * self.ON_premium_price
                    car_sell = amount * self.ON_premium_price
            print(f"Zatankowałeś {amount}l. E95 za {car_sell:.2f} zł. Stan karty lojalnościowej: {self.loyality_club[plate]}")

    def gas_fuel_post(self):
        print("Dostępne paliwa:")
        if self.E95_supply > 0 and self.E95_price != 0:
            print(f"\t- E95 - {self.E95_price}")
        else:
            print(f"\t- E95 - BRAK")
        if self.E98_supply > 0 and self.E98_price != 0:
            print(f"\t- E98 - {self.E98_price}")
        else:
            print(f"\t- E98 - BRAK")
        if self.ON_supply > 0 and self.ON_price != 0:
            print(f"\t- ON - {self.ON_price}")
        else:
            print(f"\t- ON - BRAK")
        if self.ON_premium_supply > 0 and self.ON_premium_price != 0:
            print(f"\t- ON premium - {self.ON_premium_price}")
        else:
            print(f"\t- ON premium - BRAK")

    def gas_station_account(self):
        return f"""Kwota zakupu paliw od rafinerii: {self.gas_buy:.2f}
Kwota ze sprzedaży paliw: {self.gas_sell:.2f}"""


if __name__ == "__main__":
    Shell_Wolska = Gas_Station()
    Shell_Wolska.gas_station_pumping_and_balance(type_of_fuel="E95", amount=2000, price=4.50)
    Shell_Wolska.gas_station_pumping_and_balance(type_of_fuel="E98", amount=500, price=5.00)
    Shell_Wolska.gas_station_pumping_and_balance(type_of_fuel="ON", amount=1000, price=4.75)
    print(Shell_Wolska.gas_station_pumping_and_balance(type_of_fuel="ON_premium", amount=250, price=5.00))
    Shell_Wolska.gas_price_car(type_of_fuel="E95", price=4.99)
    Shell_Wolska.gas_price_car(type_of_fuel="E98", price=5.20)
    Shell_Wolska.gas_price_car(type_of_fuel="ON", price=5.14)
    print()
    Shell_Wolska.gas_fuel_post()
    print()
    Shell_Wolska.car_refuelling(type_of_fuel="E95", amount=45, plate="WA69683")
    Shell_Wolska.car_refuelling(type_of_fuel="E95", amount=55, plate="WA69683")
    Shell_Wolska.car_refuelling(type_of_fuel="E95", amount=901, plate="WA69683")
    Shell_Wolska.car_refuelling(type_of_fuel="E95", amount=1001, plate="WA69683")
    Shell_Wolska.car_refuelling(type_of_fuel="ON", amount=60, plate="WE83396")
    Shell_Wolska.car_refuelling(type_of_fuel="ON_premium", amount=60, plate="WE83396")
    print()
    print(Shell_Wolska.gas_station_pumping_and_balance(type_of_fuel="E95", amount=0, price=4.50))
    print()
    Shell_Wolska.gas_fuel_post()
    print()
    print(Shell_Wolska.gas_station_pumping_and_balance(type_of_fuel="E95", amount=2600, price=4.50))
    print()
    Shell_Wolska.car_refuelling(type_of_fuel="ON", amount=60, plate="Brak")
    print()
    print(Shell_Wolska.gas_station_account())