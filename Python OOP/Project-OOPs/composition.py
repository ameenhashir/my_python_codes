class Salary:
    def __init__(self, salary, bonus):
        self.__salary = salary
        self.__bonus = bonus

    def total_salary(self):
        return self.__salary * 12 + self.__bonus


class Employee:
    def __init__(self, name, salary, bonus):
        self.__name = name
        self.__salary_obj = Salary(salary, bonus)

    def annual_salary(self):
        return self.__salary_obj.total_salary()


ameen = Employee('ameen', 17000, 17000)
print(ameen.annual_salary())
