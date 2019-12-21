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