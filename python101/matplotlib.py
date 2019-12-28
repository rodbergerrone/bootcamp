# import pylab
#
# x = [1, 2, 3]
# y = [4, 6, 5]
# pylab.plot(x, y)
# pylab.show()

import pylab

a = 1
b = 2
x = range(-10, 11)  # lista argumentów x

y = []  # lista wartości
for i in x:
    y.append(a * i + b)

pylab.plt(x, y)
plt.title('Wykres f(x) = a*x - b')
plt.grid(True)
plt.show()