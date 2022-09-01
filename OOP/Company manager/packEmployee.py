'''
PROBLEM:
Create an hierarchy of classes - abstract class Employee 
and subclasses HourlyEmployee, SalariedEmployee, Manager 
and Executive. Every one's pay is calculated differently,
research a bit about it. After you've established an 
employee hierarchy, create a Company class that allows you 
to manage the employees. You should be able to hire, fire 
and raise employees.

RESOLUTION:
* Hourly employees -> hourly rate and pay() are weekly

* Salaried employees -> annual salary and pay() are weekly

* Manager employees -> weekly bonus and pay() are weekly

* Executive employees -> weekly bonus, incentives and pay() are weekly
'''
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, age, sector):
        self._name = name
        self._age = age
        self._sector = sector
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @property
    def sector(self):
        return self._sector
    
    @abstractmethod
    def pay(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, name, age, sector, hourly_rate=0, hours_worked=0):
        super().__init__(name, age, sector)
        self._hourly_rate = hourly_rate
        self._hours_worked = hours_worked
    
    def __repr__(self):
        return 'Hourly'
    
    @property
    def hourly_rate(self):
        return self._hourly_rate
    
    @hourly_rate.setter
    def hourly_rate(self, hourly_rate):
        if not isinstance(hourly_rate, (float, int)):
            raise ValueError('Hourly rate need to be a integer/float!...')
        
        self._hourly_rate = hourly_rate
    
    @property
    def hours_worked(self):
        return self._hours_worked

    @hours_worked.setter
    def hours_worked(self, hours_worked):
        if not isinstance(hours_worked, int):
            raise ValueError('Hours need to be a integer!...')
        
        self._hours_worked = hours_worked

    def pay(self):
        if self.hours_worked <= 40:
            return self.hourly_rate * self.hours_worked
        else:
            return (self.hourly_rate * 1.5) * self.hours_worked

    def payment_slip(self):
        if self.hours_worked <= 40:
            print(35 * '-')
            print('\tEMPLOYEE PAYMENT SLIP')
            print(35 * '-')
            print('Employee type: Hourly')
            print(f'Name: {self.name}')
            print(f'Age: {self.age} years')
            print(f'Sector: {self._sector}')
            print(f'Hours worked: {self.hours_worked} hours')
            print(f'Total received this week: ${round(self.pay(), 2)}')
        else:
            print(35 * '-')
            print('\tEMPLOYEE PAYMENT SLIP')
            print(35 * '-')
            print('Employee type: Hourly')
            print(f'Name: {self.name}')
            print(f'Age: {self.age} years')
            print(f'Sector: {self._sector}')
            print(f'Hours worked: {self.hours_worked} hours')
            print(f'Overtime: {self.hours_worked - 40} hours')
            print(f'Total received this week: ${round(self.pay(), 2)}')

class SalariedEmployee(Employee):
    def __init__(self, name, age, sector, annual_salary=None):
        super().__init__(name, age, sector)
        self._annual_salary = annual_salary
    
    def __repr__(self):
        return 'Salaried'
    
    @property
    def annual_salary(self):
        return self._annual_salary
    
    @annual_salary.setter
    def annual_salary(self, annual_salary):
        if not isinstance(annual_salary, (float, int)):
            raise ValueError('Annual salary need to be a integer/float!...')
        
        self._annual_salary = annual_salary
    
    def pay(self):
        if not self.annual_salary == None:
            return self.annual_salary / 52
        else:
            raise ValueError('Annual salary needs to be a number!...')
    
    def payment_slip(self):
        print(35 * '-')
        print('\tEMPLOYEE PAYMENT SLIP')
        print(35 * '-')
        print('Employee type: Salaried')
        print(f'Name: {self.name}')
        print(f'Age: {self.age} years')
        print(f'Sector: {self._sector}')
        print(f'Total received this week: ${round(self.pay(), 2)}')

class ManagerEmployee(SalariedEmployee):
    def __init__(self, name, age, sector, annual_salary=None, bonus=None):
        super().__init__(name, age, sector, annual_salary)
        self._bonus = bonus
    
    def __repr__(self):
        return 'Manager'
    
    @property
    def bonus(self):
        return self._bonus
    
    @bonus.setter
    def bonus(self, bonus):
        if not isinstance(bonus, (int, float)):
            raise TypeError('Bonus needs to be integer/float!...')

        self._bonus = bonus
    
    def pay(self):
        if not self.annual_salary == None and not self.bonus == None:
            return super().pay() + self.bonus
        
        raise ValueError('Annual salary and bonus needs to be integer/float!...')
    
    def payment_slip(self):
        print(35 * '-')
        print('\tEMPLOYEE PAYMENT SLIP')
        print(35 * '-')
        print('Employee type: Manager')
        print(f'Name: {self.name}')
        print(f'Age: {self.age} years')
        print(f'Sector: {self._sector}')
        print(f'Total received this week: ${round(self.pay(), 2)}')

class ExecutiveEmployee(ManagerEmployee):
    def __init__(self, name, age, sector, annual_salary=None, bonus=None, incentives=None):
        super().__init__(name, age, sector, annual_salary, bonus)
        self._incentives = incentives
    
    def __repr__(self):
        return 'Executive'
    
    @property
    def incentives(self):
        return self._incentives
    
    @incentives.setter
    def incentives(self, incentives):
        if not isinstance(incentives, (int, float)):
            raise TypeError('Incentives needs to be integer/float!...')

        self._incentives = incentives
    
    def pay(self):
        if not self.annual_salary == None and not self.bonus == None:
            return (super().pay() * self.incentives) + self.bonus 
        
        raise ValueError('Annual salary and bonus needs to be integer/float!...')
    
    def payment_slip(self):
        print(35 * '-')
        print('\tEMPLOYEE PAYMENT SLIP')
        print(35 * '-')
        print('Employee type: Executive')
        print(f'Name: {self.name}')
        print(f'Age: {self.age} years')
        print(f'Sector: {self._sector}')
        print(f'Total received this week: ${round(self.pay(), 2)}')