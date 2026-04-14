# concept :  Abstraction
#Create an abstract class Employee  with an abstract method  calculate_salary() method. Create subclasses INTERN, FULLTIME, and ContractEmployee that implement the calculate_salary() method differently.


from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend

    def calculate_salary(self):
        print(f"Intern Salary (Stipend): {self.stipend}")

class FullTime(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        print(f"Full-Time Employee Salary: {self.monthly_salary}")

class ContractEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        salary = self.hourly_rate * self.hours_worked
        print(f"Contract Employee Salary: {salary}")

# Create instances of each employee type and calculate their salaries
intern = Intern(1500)
full_time_employee = FullTime(5000)
contract_employee = ContractEmployee(20, 160)
intern.calculate_salary()
full_time_employee.calculate_salary()
contract_employee.calculate_salary()

