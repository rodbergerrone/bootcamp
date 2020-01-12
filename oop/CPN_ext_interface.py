from collections import defaultdict

# TODO: z oop ex-04.py
class Car:
    def __init__(self):
        self._zatankowane = 0

    @property
    def rabat(self):
        if self._zatankowane > 1000:
            discount = 0.1
        else:
            discount = 0


class Gas_Station:
    def __init__(self, nazwa, adres):
        self.nazwa = nazwa
        self.adres = adres
        self.E95_supply = 0
        self.E98_supply = 0
        self.ON_supply = 0
        self.ON_premium_supply = 0
        self.E95_price = 0
        self.E98_price = 0
        self.ON_price = 0
        self.ON_premium_price = 0
        self.loyality_club = defaultdict(int)
        self.gas_buy = 0
        self.gas_sell = 0

    def gas_station_supplies(self):
        return f"""Stan poszczególnych paliw:
\t- E95 - {self.E95_supply} litrów;
\t- E98 - {self.E98_supply} litrów;
\t- ON - {self.ON_supply} litrów;
\t- ON premium - {self.ON_premium_supply} litrów."""

    def gas_station_pumping(self, type_of_fuel, amount, price):
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

    def gas_price_car(self, type_of_fuel, price):
        if type_of_fuel == "E95":
            self.E95_price = price
        if type_of_fuel == "E98":
            self.E98_price = price
        if type_of_fuel == "ON":
            self.ON_price = price
        if type_of_fuel == "ON_premium":
            self.ON_premium_price = price

    #TODO: albo tutaj
    def discuont(self):
        if self._zatankowane > 1000:
            return 0.1
        else:
            return 0

    def car_refuelling(self, type_of_fuel, amount, plate):
        # if self.E95_supply == 0 or self.E98_supply == 0 or self.ON_supply == 0 or self.ON_supply_supply == 0:
        #     print("Sprzedaż niemożliwa")
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
            else:
                self.loyality_club[plate] += amount
                if self.loyality_club[plate] >= 1000:
                    self.gas_sell += amount * self.ON_premium_price
                    car_sell = amount * (self.ON_premium_price - 0.10)
                else:
                    self.gas_sell += amount * self.ON_premium_price
                    car_sell = amount * self.ON_premium_price
            print(f"Zatankowałeś {amount}l. E95 za {car_sell:.2f} zł. Stan karty lojalnościowej: {self.loyality_club[plate]}")

    def gas_station_price_post(self):
        print("Dostępne paliwa:")
        if self.E95_supply > 0 and self.E95_price != 0:
            print(f"\t- E95 - {self.E95_price} PLN")
        else:
            print(f"\t- E95 - BRAK")
        if self.E98_supply > 0 and self.E98_price != 0:
            print(f"\t- E98 - {self.E98_price} PLN")
        else:
            print(f"\t- E98 - BRAK")
        if self.ON_supply > 0 and self.ON_price != 0:
            print(f"\t- ON - {self.ON_price} PLN")
        else:
            print(f"\t- ON - BRAK")
        if self.ON_premium_supply > 0 and self.ON_premium_price != 0:
            print(f"\t- ON premium - {self.ON_premium_price} PLN")
        else:
            print(f"\t- ON premium - BRAK")

    def gas_station_accounts(self):
        return f"""Kwota zakupu paliw od rafinerii: {self.gas_buy:.2f}
Kwota ze sprzedaży paliw: {self.gas_sell:.2f}"""


Shell_Wolska = Gas_Station(nazwa="Shell", adres="ul. Wolska 190, Warszawa")
while True:
    print(f"""Program obsługi stacji {Shell_Wolska.nazwa, Shell_Wolska.adres}. Dostępne działania:
- (u)zupełnienie paliwa
- (c)eny paliw
- (s)rzedaż paliw
- (o)broty stacji
- (z)apasy paliw""")
    wybor = input("Co chcesz zrobić?")
    if wybor == "u":
        print(Shell_Wolska.gas_station_supplies())
        Shell_Wolska.gas_station_pumping(type_of_fuel=input("Podaj typ paliwa (E95/E98/ON/ON_premium):"), amount=float(input("Podaj ilość:")), price=float(input("Podaj cenę zakupu:")))
    if wybor == "c":
        Shell_Wolska.gas_price_car(type_of_fuel=input("Podaj typ paliwa (E95/E98/ON/ON_premium):"), price=float(input("Podaj cenę sprzedaży:")))
        Shell_Wolska.gas_station_price_post()
    if wybor == "s":
        Shell_Wolska.car_refuelling(type_of_fuel=input("Podaj typ paliwa (E95/E98/ON/ON_premium):"), amount=float(input("Podaj ilość:")), plate=input("Podaj nr rejestracyjny lub Brak:"))
    if wybor == "o":
        print(Shell_Wolska.gas_station_accounts())
    if wybor == "z":
        print(Shell_Wolska.gas_station_supplies())


# TODO: 1. sprzedaż niemożliwa jak nie ma paliwa