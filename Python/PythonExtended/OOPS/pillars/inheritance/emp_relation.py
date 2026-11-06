class Employee:

    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def describe(self):
        return f"Name {self.name} | Salary {self.salary:.0f}"

    def annual_cost(self):
        return self.salary*12


class Manager(Employee): # Manager Inherits Employee

    def __init__(self, name, salary,reports):
        super().__init__(name, salary) # name and salary are inherited from parent
        self.reports = reports # this attribute is exclusive to Manager class


    # Overriding: same method name: diff behaviour
    def describe(self):

        desc = super().describe()
        return f"{desc}, manages {len(self.reports)} people"

    # this is method() is exclusive to Manager class
    def add_report(self, employee):
        self.reports.append(employee)


aditi_emp = Employee("Aditi",60_000)
aditya_emp = Employee("Aditya",40_000)

sushila_emp = Manager("Sushila", 100_000,[aditi_emp])
sushila_emp.add_report(aditi_emp)

print(sushila_emp.annual_cost())
print(aditi_emp.annual_cost())
print(sushila_emp.describe())
# print(aditi_emp.add_report(sushila_emp))

print()
print(isinstance(aditi_emp,Employee))
print(isinstance(aditi_emp,Manager))
print(isinstance(sushila_emp,Employee))
print(isinstance(sushila_emp,Manager))
print()



print(issubclass(Employee,Manager))
print(issubclass(Manager,Employee))


