class Employee:
    total_employee = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def employee_add(self):
        print(f"New Employee ,{self.name}, You are most Welcomed with salary ,{self.salary}")
        Employee.total_employee = Employee.total_employee + 1
        print(f"Total Employee {Employee.total_employee}")
emp1 = Employee("VIGHNESH",9000000)
emp2 = Employee("VICKYY",5000000)
emp3 = Employee("VIGSSSS",5265000)
emp1.employee_add()
emp2.employee_add()
emp3.employee_add()
