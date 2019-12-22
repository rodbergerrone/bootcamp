class Employee:
    def __init__(self, name, surname, rate_per_hour):
        self.name = name
        self.surname = surname
        self.rate_per_hour = rate_per_hour
        self._salary_to_pay = 0

    def register_time(self, time):
        if time > 8:
            self._salary_to_pay += 8 * self.rate_per_hour
            self._salary_to_pay += (time - 8) * 2 * self.rate_per_hour
        else:
            self._salary_to_pay += time * self.rate_per_hour

    def pay_salary(self):
        result = self._salary_to_pay
        self._salary_to_pay = 0
        return result

class PremiumEmployee(Employee):
    def __init__(self, name, surname, rate_per_hour):
        super().__init__(name, surname, rate_per_hour)
        self._bonuses = 0

    def give_bonus(self, bonus_value):
         self._bonuses += bonus_value

    def pay_salary(self):
        result = super().pay_salary()
        result += self._bonuses
        self._bonuses = 0
        return result


if __name__ == "__main__":
    employee = Employee("Jan", "Nowak", 100.0)
    employee.register_time(7)
    #print("Hacking!", employee._salary_to_pay")
    print(employee.pay_salary())
    print(employee.pay_salary())
    employee.register_time(11)
    print(employee.pay_salary())
    employee.register_time(5)
    employee.register_time(5)
    print(employee.pay_salary())
    employee = PremiumEmployee("Jan", "Nowak", 100.0)
    employee.give_bonus(1000)
    print(employee.pay_salary())
    print(employee.pay_salary())