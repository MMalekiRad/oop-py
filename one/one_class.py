class Employee:
    """Common base class for all employees"""

    # property
    empCount = 0

    # constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    # method
    def displayCount(self):
        print("Total Employee %d" % self.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


pass


class NewClass:
    print("This is New Class")
    pass


print("one_class.py is here!")

# obj = Employee("Amir", 190000)
# obj.displayEmployee()
# obj.displayCount()
