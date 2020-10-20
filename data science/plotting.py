from matplotlib import pyplot as plt
from matplotlib import style

# x = [1, 2, 3, 4]
# y = [25, 10, 5, 5]
#
# x2 = [1, 2, 3, 4]
# y2 = [22, 11, 6, 6]
#
# plt.plot(x, y, 'g', label='price in 2020', linewidth=4)
# plt.plot(x2, y2, 'c', label='price in 2019', linewidth=4)
#
# plt.title('Paprika price 2019-20')
# plt.ylabel('Price PLN/kg')
# plt.xlabel('Quater of year')
#
# plt.legend()
# plt.grid(True, color='k')
#
# plt.show()

style.use("ggplot")

x = [1, 2, 3, 4]
y = [25, 10, 5, 5]

x2 = [1, 2, 3, 4]
y2 = [22, 11, 6, 6]

plt.plot(x,y,'r')
plt.plot(x2,y2,'b')

plt.title("Info no 2")
plt.ylabel("Price")
plt.xlabel("Quater")

plt.show()