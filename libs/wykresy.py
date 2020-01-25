# import pylab
#
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = [4.5, 6, 5.55, 4.33, 3.0, 3.5, 4, 4.1, 4.2, 4.5]
# pylab.plot(x, y)
# pylab.show()

import pylab

a = 1
b = 2
x = [i for i in range(-10, 11)]  # lista argumentów x

y = []  # lista wartości
for i in x:
    y.append(a * i + b)

pylab.plot(x, y)
pylab.title('Wykres f(x) = a*x - b')
pylab.grid(True)
pylab.show()