class Employee:

    def __init__(self, name: str = 'Name', position: str = 'position', salary: int = 0):
        self.Name = name
        self.Position = position
        self.Salary = salary

    def __str__(self):
        return (f'{self.Name}\n'
                f'\tPosition: {self.Position}\n'
                f'\tSalary: {self.Salary}')

    def Get_Salary(self):
        return self.Salary