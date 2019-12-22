class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y)
        else:
            return Vector(self.x * other, self.y * other)

    def __eq__(self, other):
        # porównanie po x i y
        # return self.x == other.x and self.y == other.y
        # porównanie po długości
        return (self.x ** 2 + self.y ** 2) == (other.x ** 2 + other.y ** 2)

if __name__ == "__main__":
    v1 = Vector(1, 3)
    v2 = Vector(3, 1)
    v3 = v1 + v2
    print("Dodawanie:", v1 + v2)
    print("Odejmowanie:", v1 - v2)
    print("Mnożenie_liczba:", v1 * 3)
    print("Mnożenie_vektor:", v1 * v2)
    print("Porównywanie:", v1 == v2)
    print("Porównywanie:", v1 == v3)