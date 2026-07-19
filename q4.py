# 4.	Create an Employee class and calculate annual salary from monthly salary.

# Create Class
class Employee:
    def __init__(self, salary=0):
        self.salary = salary

    def annual_salary(self):
        return 12 * self.salary
    
    def display_details(self):
        print("Salary Details:")
        print("----------------")
        print("Monthly Salary :", self.salary)
        print("Annual (12 Months) Salary :", self.annual_salary())

# Create Object
employee1 = Employee(10000)

# Display Details
employee1.display_details()

        
