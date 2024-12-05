from Employee import Employee


class Department:
    Employees = list()
    Department_Name = None

    def __init__(self, department_name: str = 'department name'):
        self.Department_Name = department_name

    def Add_Employees(self, employee: Employee):
        if isinstance(employee, Employee):
            self.Employees.append(employee)
        else:
            print('This is not Employee, try again')

    def Fire_Employees(self, employee: Employee):
        if isinstance(employee, Employee):
            self.Employees.remove(employee)
        else:
            print('This is not Employee, try again')

    def getInfoSalary(self):
        money = 0
        for i in self.Employees:
            person_money = i.Get_Salary() #200 300 100
            money = money + person_money
        return money


    def __str__(self):
        string = f'Department name: {self.Department_Name}\nLIST OF EMPLOYEES:\n'
        for i in self.Employees:
            string = string + str(i) + '\n'
        return string + '\n'
