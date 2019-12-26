class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Produkt {self.name!r}, id: {self.id}, cena: {self.price} PLN"

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
        result = "Zawartość kosztyka:"
        for product, quantity in self._products.items():
            result += f"\n- {product.name} ({product.id}): {product.price} PLN x {quantity} szt."
        result += f"\nW sumie: {self.count_total_price()} PLN"
        return result

    @classmethod
    def from_products(cls, given_products):
        basket = cls()
        for product in given_products:
            basket.add_product(product, 1)
        return basket


def test_generate_report_water():
    woda = Product(1, "Woda", 10)
    basket = Basket()
    basket.add_product(woda, 5)
    expected = """Zawartość kosztyka:
- Woda (1): 10 PLN x 5 szt.
W sumie: 50 PLN"""
    assert basket.generate_report() == expected

def test_basket_from_products():
    p1 = Product(1, "Woda", 4)
    p2 = Product(2, "Chleb", 3)
    p3 = Product(4, "Rybka", 10)
    b = Basket.from_products([p1, p2, p3])
    assert isinstance(b, Basket)
    assert len(b.generate_report().splitlines()) == 2 + 3

def test_basket_empty_price():
    b = Basket()
    assert b.count_total_price() == 0

def test_basket_one_product_price():
    b = Basket()
    p = Product(1, 'Woda', 10.00)
    b.add_product(p, 3)
    assert b.count_total_price() == 3 * 10

def test_basket_multiple_products_price():
    b = Basket()
    woda = Product(1, 'Woda', 10.00)
    chleb = Product(2, 'Chleb', 20.00)
    b.add_product(woda, 3)
    b.add_product(chleb, 1)
    b.add_product(woda, 1)
    assert b.count_total_price() == 4 * 10 + 1 * 20

def test_basket_one_product_report():
    b = Basket()
    p = Product(1, 'Woda', 10)
    b.add_product(p, 3)
    expected = """Zawartość kosztyka:
- Woda (1): 10 PLN x 3 szt.
W sumie: 30 PLN"""
    assert b.generate_report() == expected

def test_basket_multiple_products_report():
    b = Basket()
    p1 = Product(1, 'Pierogi', 10.00)
    p2 = Product(2, 'Choinka', 20.00)
    p3 = Product(3, 'Prezenty', 30.00)
    b.add_product(p1, 10)
    b.add_product(p2, 1)
    b.add_product(p3, 4)
    assert len(b.generate_report().splitlines()) == 2 + 3

def test_basket_from_products():
    p1 = Product(1, 'Pierogi', 10.00)
    p2 = Product(2, 'Choinka', 20.00)
    p3 = Product(3, 'Prezenty', 30.00)
    b = Basket.from_products([p1, p2, p3])  # użyć @classmethod
    assert isinstance(b, Basket)
    assert len(b.generate_report().splitlines()) == 2 + 3


if __name__ == "__main__":
    woda = Product(1, "Woda", 4)
    chleb = Product(2, "Chleb", 3)
    choinka = Product(3, "Chionka", 100)
    rybka = Product(4, "Rybka", 10)
    basket = Basket()
    basket.add_product(woda, 5)
    basket.add_product(chleb, 4)
    basket.add_product(choinka, 1)
    basket.add_product(rybka, 4)
    # print(basket.count_total_price())
    print(basket.generate_report())