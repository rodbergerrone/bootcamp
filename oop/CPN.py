j# Zadanie Domowe: Stacja Paliw
# Zaimplementuj klasę StacjaPaliw umożliwiającą obsługę stacji paliw. Klasa powinna posiadać metody umożliwiające
# uzupełnienie zapasów paliwa, ustalenie ceny danego paliwa, zatankowanie samochodu oraz generowanie tablicy dostępnych
# paliw wraz z cenami. Zaimplementuj zestaw testów oraz interfejs tekstowy wykorzystujący stworzoną klasę.
# Paliwo jest dostępne do sprzedaży kiedy stacja posiada je w swoich zapasach oraz jest ustalona jego cena.

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

    def station_pumping(self, type_of_fuel, amount):
        if type_of_fuel == "E95":
            self.E95_supply += amount
        if type_of_fuel == "E98":
            self.E98_supply += amount
        if type_of_fuel == "ON":
            self.ON_supply += amount
        if type_of_fuel == "ON_premium":
            self.ON_premium_supply += amount
        return f"""Stan poszczególnych paliw:
\t- E95 - {self.E95_supply} litrów;
\t- E98 - {self.E98_supply} litrów;
\t- ON - {self.ON_supply} litrów;
\t- ON premium - {self.ON_premium_supply} litrów."""

    def gas_price(self, type_of_fuel, price):
        if type_of_fuel == "E95":
            self.E95_price = price
        if type_of_fuel == "E98":
            self.E98_price = price
        if type_of_fuel == "ON":
            self.ON_price = price
        if type_of_fuel == "ON_premium":
            self.ON_premium_price = price

    def car_refuelling(self, type_of_fuel, amount):
        if type_of_fuel == "E95" and self.E95_price != 0:
            self.E95_supply -= amount
            print(f"Zatankowałeś {amount} l. E95 za {amount * self.E95_price} zł")
        if type_of_fuel == "E98" and self.E98_price != 0:
            self.E98_supply -= amount
            print(f"Zatankowałeś {amount} l. E98 za {amount * self.E98_price} zł")
        if type_of_fuel == "ON" and self.ON_price != 0:
            self.ON_supply -= amount
            print(f"Zatankowałeś {amount} l. ON za {amount * self.ON_price} zł")
        if type_of_fuel == "ON_premium" and self.ON_premium_price != 0:
            self.ON_premium_supply -= amount
            print(f"Zatankowałeś {amount} l. ON premium za {amount * self.ON_premium_price} zł")

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


if __name__ == "__main__":
    Shell_Wolska = Gas_Station()
    Shell_Wolska.station_pumping(type_of_fuel="E95", amount=2000)
    Shell_Wolska.station_pumping(type_of_fuel="E98", amount=500)
    Shell_Wolska.station_pumping(type_of_fuel="ON", amount=1000)
    print(Shell_Wolska.station_pumping(type_of_fuel="ON_premium", amount=250))
    Shell_Wolska.gas_price(type_of_fuel="E95", price=4.99)
    Shell_Wolska.gas_price(type_of_fuel="E98", price=5.20)
    Shell_Wolska.gas_price(type_of_fuel="ON", price=5.14)
    print()
    Shell_Wolska.gas_fuel_post()
    print()
    Shell_Wolska.car_refuelling(type_of_fuel="E95", amount=45)
    Shell_Wolska.car_refuelling(type_of_fuel="ON", amount=60)
    Shell_Wolska.car_refuelling(type_of_fuel="ON_premium", amount=60)
    print()
    print(Shell_Wolska.station_pumping(type_of_fuel="E95", amount=0))