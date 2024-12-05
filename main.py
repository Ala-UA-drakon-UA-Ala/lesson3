"""
Завдання 4: Розробіть систему для керування персоналом компанії.
Створіть клас Employee з властивостями, такими як ім'я, посада, заробітна плата тощо.
Створіть клас Department, який буде містити список співробітників і методи для додавання, видалення співробітників
і підрахунку загальної заробітної плати відділу.
"""

from Department import Department
from Employee import Employee

Ivan_Ivanovich = Employee('Ivan Ivanovich Ivanovskiy', 'manager', 45000)
Petya_Petyovich = Employee('Petya Petyovich Petyovskiy', 'worker', 25000)
Oleg_Olegovich = Employee('Oleg Olegovich Olegovskiy', 'worker', 30000)

Law_Department = Department('Law Department')
print("Add employees")
Law_Department.Add_Employees(Ivan_Ivanovich)
Law_Department.Add_Employees(Petya_Petyovich)
Law_Department.Add_Employees(Oleg_Olegovich)
Law_Department.Add_Employees(3)
print(Law_Department)

print("Remove employee")
Law_Department.Fire_Employees(Petya_Petyovich)
print(Law_Department)

print(f'Emploees salary: {Law_Department.getInfoSalary()}')