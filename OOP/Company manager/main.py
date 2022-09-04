from packEmployee import HourlyEmployee, SalariedEmployee, ManagerEmployee, ExecutiveEmployee
from packCompany import Company

company = Company('PomPom', 50000.00)
e1 = HourlyEmployee('Viktor', 20, 'Cleaner', 10.5, 50)
company.hire(e1)

print()

company.show_employees()


print()

company.raise_(e1, 'manager', annual_salary=50000.00, bonus=15)

print()
    
company.show_employees()

print()

company.employees[0].payment_slip()