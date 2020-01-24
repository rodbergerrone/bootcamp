import time

time.strftime('%Y.%m.%d %H:%M:%S %Z')

t1 = time.time() # w sekundach
t2 = time.time()
print(t2 - t1)

print(time.asctime())

time.sleep(2) # w sekundach


import datetime

d1 = datetime.datetime(2000, 1, 1, 13, 00)
d2 = datetime.datetime.now()
print("Delta:", d2 - d1)

datetime.timedelta
if datetime.date(1983, 12, 12).weekday() == 0:
    print("You were born on Monday.")


import itertools


import decimal

d = decimal.Decimal(1)


import os

print(os.path.exists('car.json'))