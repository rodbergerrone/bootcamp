class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        print(f"Produkt {self.name!r}, id: {self.id}, cena: {self.price} PLN")

class Basket:
    def __init__(self):
        self._products = {}

    def add_product(self, produkt, quantity):
        # key == produkt
        if produkt in self._products:
            self._products[produkt] += quantity
        else:
            self._products[produkt] = quantity

    def count_total_price(self):
        total_price = 0
        for product, quantity in self._products.items():
            total_price += product.price * quantity
        return total_price

    def generate_report(self):
        return f"Produkty w koszyku: \n-{produkt} ({self.id}), cena: {self.price} x {self.quantity}\nW sumie: {self.total_price}"

if __name__ == "__main__":
    woda = Product(1, "Woda", 10)
    chleb = Product(1, "Chleb", 20)
    basket = Basket()
    basket.add_product(woda, 5)
    basket.add_product(chleb, 1)
    basket.add_product(woda, 3)
    print(basket.count_total_price())
    print(basket.generate_report())