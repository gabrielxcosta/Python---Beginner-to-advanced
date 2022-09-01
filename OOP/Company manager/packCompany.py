'''
PROBLEM:
Create an hierarchy of classes - abstract class Employee 
and subclasses HourlyEmployee, SalariedEmployee, Manager 
and Executive. Every one's pay is calculated differently,
research a bit about it. After you've established an 
employee hierarchy, create a Company class that allows you 
to manage the employees. You should be able to hire, fire 
and raise employees.
'''
from packEmployee import HourlyEmployee, SalariedEmployee, ManagerEmployee, ExecutiveEmployee

class Company:
    def __init__(self, corporate_name, amount):
        self._corporate_name = corporate_name
        self._amount = amount
        self._employees = []
    
    @property
    def corporate_name(self):
        return self._corporate_name
    
    @property
    def amount(self):
        return self._amount
    
    @property
    def employees(self):
        return self._employees

    def hire(self, employee):
        if not isinstance(
            employee, 
            (HourlyEmployee,
            SalariedEmployee,
            ManagerEmployee,
            ExecutiveEmployee)
            ):
            raise ValueError("Employee needs to be a instance of Employee's class")
        
        self.employees.append(employee)
        print(f'{employee.name} was hired...')
    
    def fire(self, employee):
        if not isinstance(
            employee, 
            (HourlyEmployee,
            SalariedEmployee,
            ManagerEmployee,
            ExecutiveEmployee)
            ):
            raise ValueError("Employee needs to be a instance of Employee's class")
        
        aux = 0
        for index, emp in enumerate(self.employees):
            if emp.name == employee.name:
                aux = index

        fired = self.employees.pop(index)
        print(f'{fired.name} was fired...')
    
    def raise_(self, employee, rank, **kwargs):
        if not isinstance(
            employee, 
            (HourlyEmployee,
            SalariedEmployee,
            ManagerEmployee,
            ExecutiveEmployee)
            ):
            raise ValueError("Employee needs to be a instance of Employee's class")

        aux = 0
        for index, emp in enumerate(self.employees):
            if emp.name == employee.name:
                aux = index
        
        if rank == 'hourly':
            print("The employee cannot be elevated to a lower rank!...")
            return
        elif rank == 'salaried':
            if isinstance(self.employees[aux], HourlyEmployee):
                raised = self.employees.pop(aux)
                raised = SalariedEmployee(
                    raised.name, 
                    raised.age, 
                    raised.sector,
                    kwargs.get('annual_salary')
                )

                self.employees.append(raised)
                print(f'{raised.name} was elevated to salaried...')
            else:
                print("Invalid request!...")
                return
        elif rank == 'manager':
            if isinstance(self.employees[aux], (HourlyEmployee, SalariedEmployee)):
                raised = self.employees.pop(aux)
                raised = ManagerEmployee(
                    raised.name, 
                    raised.age, 
                    raised.sector,
                    kwargs.get('annual_salary'),
                    kwargs.get('bonus')
                )

                self.employees.append(raised)
                print(f'{raised.name} was elevated to manager..')
            else:
                print("Invalid request!...")
                return        
        elif rank == 'executive':
            if isinstance(self.employees[aux], (HourlyEmployee, SalariedEmployee, ManagerEmployee)):
                raised = self.employees.pop(aux)
                raised = ExecutiveEmployee(
                    raised.name, 
                    raised.age, 
                    raised.sector,
                    kwargs.get('annual_salary'),
                    kwargs.get('bonus'),
                    kwargs.get('incentives')
                )

                self.employees.append(raised)
                print(f'{raised.name} was elevated to manager..')
            else:
                print("Invalid request!...")
                return        
        else:
            raise ValueError('Level needs to be: hourly, salaried, manager or executive!...')
    
    def show_employees(self):
        if not self.employees == []:
            print(35 * '-')
            print('\tEMPLOYEE(S) LIST')
            print(35 * '-')
            for employee in self.employees:
                print(f'Type employee: {employee.__repr__()}')
                print(f'Name: {employee.name}')
                print(f'Age: {employee.age} years')
                print(f'Sector: {employee.sector}')
        else:
            print('The company has no employees!...')