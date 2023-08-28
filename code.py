class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []
        
    def add_employee(self, emp):
        self.employees.append(emp)
        
    def sort_by_age(self):
        self.employees.sort(key=lambda emp: emp.age)
        
    def sort_by_name(self):
        self.employees.sort(key=lambda emp: emp.name)
        
    def sort_by_salary(self):
        self.employees.sort(key=lambda emp: emp.salary)
        
    def display_table(self):
        for emp in self.employees:
            print(f"{emp.emp_id}\t{emp.name}\t{emp.age}\t{emp.salary}")

if __name__ == "__main__":
    emp_table = EmployeeTable()
    
    emp_table.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_table.add_employee(Employee("171G30", "Ajay", 45, 44000))
    
    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    
    choice = int(input())
    
    if choice == 1:
        emp_table.sort_by_age()
    elif choice == 2:
        emp_table.sort_by_name()
    elif choice == 3:
        emp_table.sort_by_salary()
    else:
        print("Invalid choice")
    
    print("\nSorted Employee Table:")
    print("Emp ID\tName\tAge\tSalary")
    emp_table.display_table()
