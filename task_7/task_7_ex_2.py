"""
Task 7_2
Create classes Employee, SalesPerson, Manager and Company with predefined functionality.
Create basic class Employee and declare following content:
• Attributes – name (str), salary and bonus (int), set with property decorator
• Constructor - parameters name and salary
• Method bonus - sets bonuses to salary, amount of which is delegated as bonus
• Method to_pay - returns the value of summarized salary and bonus.
Create class SalesPerson as class Employee inheritor and declare within it:
• Constructor with parameters: name, salary, percent – percent of plan performance (int, without the % symbol), first two of which are passed from basic class constructor
• Redefine method of parent class bonus in the following way: if the sales person completed the plan more than 100%, their bonus is doubled (is multiplied by 2), and if more than 200% - bonus is tripled (is multiplied by 3)
Create class Manager as Employee class inheritor, and declare within it:
• Constructor with parameters: name, salary and client_number (int, number of served clients), first two of which are passed to basic class constructor.
• Redefine method of parent class bonus in the following way: if the manager served over 100 clients, their bonus is increased by 500, and if more than 150 clients – by 1000.
Create class Company and declare within it:
• Constructor with parameters: employees – list of company`s employees (made up of Employee/SalesPerson/Manager classes instances) with arbitrary length n
• Method give_everybody_bonus with parameter company_bonus (int) that sets the amount of basic bonus for each employee.
• Method total_to_pay that returns total amount of salary of all employees including awarded bonus
• Method name_max_salary that returns name of the employee, who received maximum salary including bonus.
Note:
Class attributes and methods should bear exactly the same names as those given in task description
Methods should return only target values, without detailed explanation within return
"""


class Employee:
    _bonus = 100

    def __init__(self, name, salary):
        self.__name = str(name)
        self.__salary = float(salary)
        self.__bonus = 0

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, bonus):
        self.set_bonus(bonus)

    def set_bonus(self, bonus):
        if not isinstance(bonus, int):
            raise TypeError
        self.__bonus = bonus

    def to_pay(self):
        return self.__salary + (self.__bonus if self.__bonus else 0)


class SalesPerson(Employee):
    def __init__(self, name, salary, percent=100):
        super().__init__(name, salary)
        self.__percent = percent

    def bonus(self, bonus=Employee._bonus):
        if 100 <= self.__percent < 200:
            bonus *= 2
        elif self.__percent >= 200:
            bonus *= 3
        super().set_bonus(bonus)


class Manager(Employee):
    def __init__(self, name, salary, client_number):
        super().__init__(name, salary)
        self.__client_number = client_number

    def bonus(self, bonus=Employee._bonus):
        if 100 <= self.__client_number < 150:
            bonus += 500
        elif self.__client_number >= 150:
            bonus += 1000
        super().set_bonus(bonus)


class Company:
    def __init__(self, employees, n):
        self.__employees = employees
        self.__n = n

    @property
    def employees(self):
        return self.__employees

    def give_everybody_bonus(self):
        for employee in self.__employees:
            employee.set_bonus()

    def total_to_pay(self):
        total = 0
        for employee in self.__employees:
            total += employee.to_pay()
        return total

    def name_max_salary(self):
        max_salary_employee = None
        max_salary = 0
        for employee in self.__employees:
            if employee.salary > max_salary:
                max_salary = employee.salary
                max_salary_employee = employee
        return max_salary_employee.name
