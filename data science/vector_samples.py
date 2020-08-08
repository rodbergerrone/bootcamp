# Dodawanie wektorów
def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v,w)]

# Odejmowanie wektorów
def vector_substract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v,w)]

# Sumowanie listy wektorów
def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

# Mnożenie wektora przez skalar
def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

# Średnia wektorów
def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

# Iloczyn skalarny
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

# Suma kwadratów wektorów
def sum_of_squares(v):
    return dot(v, v)

# Moduł wektora (długość)
import math


def magnitude(v):
    return math.sqrt(sum_of_squares(v))

# Dystans pomiędzy dwoma wektorami
def distance(v, w):
    return magnitude(vector_substract(v, w))


print(f"Dodawanie wektorów: {vector_add([2, 1], [2, 2])}")
print(f"Odejmowanie wektorów: {vector_substract([2, 1], [2, 2])}")
print(f"Suma wektorów: {vector_sum([[2, 1], [2, 2]])}")
print(f"Mnożenie wektora przez skalar: {scalar_multiply(3, [2, 2])}")
print(f"Średnia wektorów: {vector_mean([[2, 1], [2, 2], [6, 7]])}")
print(f"Iloczyn skalarny wektorów: {dot([2, 1], [2, 2])}")
print(f"Suma kwadratów wektorów: {sum_of_squares([2, 1])}")
print(f"Długość wektora: {magnitude([2, 1])}")
print(f"Odległośc pomiędzy wektorami: {distance([4, 6], [2, 2])}")
