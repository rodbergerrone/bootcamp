import json

# a = {'a': 1, 'b': [1, 2, 3], "Warszawa": 12.3}
# json.dumps(a)

cars = {'WZ123': 12, 'BY456': 5}
with open('cars.json', 'w') as f:
    json.dump(cars, f)