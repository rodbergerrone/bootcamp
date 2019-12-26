class ElectricCar:
    def __init__(self, car_range):
        self.car_range = car_range
        self._total_distance = 0

    def drive(self, distance):
        if distance > self.car_range - self._total_distance:
            available_distance = self.car_range - self._total_distance
            self._total_distance += available_distance
            return available_distance
        else:
            self._total_distance += distance
            return distance

    def charge(self):
        self._total_distance = 0


def test_electric_car_init():
    e = ElectricCar(100)
    assert e.car_range == 100

def test_electric_car_drive_within_range():
    e = ElectricCar(100)
    assert e.drive(80) == 80
    assert e.drive(20) == 20

def test_electric_car_drive_above_range():
    e = ElectricCar(400)
    assert e.drive(420) == 400

def test_electric_car_drive_above_range_several_parts():
    e = ElectricCar(100)
    assert e.drive(70) == 70
    assert e.drive(50) == 30
    assert e.drive(20) == 0

def test_electric_car_charge():
    e = ElectricCar(100)
    e.drive(100)
    e.charge()
    assert e.drive(120) == 100


if __name__ == "__main__":
    car = ElectricCar(100)
    car.drive(70)
    print(car._total_distance)
    car.drive(50)
    print(car._total_distance)
    car.charge()
    car.drive(50)
    print(car._total_distance)
    car.drive(50)
    print(car._total_distance)