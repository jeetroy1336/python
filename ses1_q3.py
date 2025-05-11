# Write a program in Python to demonstrate inheritance by creating two parent
# classes and one child class. 
# Define a Person class with attributes name and age, along with a method display_person_info() to print personal details
# Create an Employee class with attributes employee_id and salary, and a method display_employee_info() to print employee details.
# Define a Manager class that inherits from Person or Employee, adds an additional attribute department, and
# implements display_manager_info() to call methods from the parent class and
# display manager details. Finally, create an object of Manager, initialize
# values for all attributes, and call all methods to display complete details.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary
    def display_employee_info(self):
         print(f"Employee ID: {self.employee_id}")
         print(f"Salary: {self.salary}")
         
class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(self,  name , age)
        Employee.__init__(self, employee_id, salary)
        self.department = department
    def display_manager_info(self):
        self.display_person_info()
        self.display_employee_info()
        print(f"Department: {self.department}")
        
manager1 = Manager("Jeet", 23, 22030, 45000, "Information Technology")
manager1.display_manager_info()