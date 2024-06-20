import numpy as np
import uuid
from datetime import date, timedelta

def random_first_name() :
    """
    open first-names.txt file and returns a first name
    :return: first name
    """
    # Ensure reproducibility of measurements
    with open("/Users/Oussama/employee-management-api/fake_data/first-names.txt",'r') as f:
        names = f.readlines()
        first_name = np.random.choice(names).strip()
    return first_name

def random_last_name() -> str :
    """
    open last-names.txt file and returns a last name
    :return: last name
    """

    with open("/Users/Oussama/employee-management-api/fake_data/last-names.txt",'r') as f:
        names = f.readlines()
        last_name = np.random.choice(names).strip()
    return last_name

def random_date() -> date :
    """
    generate a random date
    :return: date
    """
    year = np.random.randint(1980,2024)
    month = np.random.randint(1,13)
    day = np.random.randint(1,28)
    return date(year,month,day)



list_department = ["HR", "IT", "SALE","MARKETING"]

class Employee:
    """
    Simulate an employee in TechCorp company
    Take an id, first name, last name, email, department, and hire date
    and create an object Employee
    """
    def __init__(self) -> None :
            self.id = uuid.uuid4()
            self.first_name = random_first_name()
            self.last_name = random_last_name()
            self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@techcorp.com"
            self.department = np.random.choice(list_department)
            self.hire_date = random_date()

    def __repr__(self) -> list:
        print(
            [self.id,
             self.first_name,
             self.last_name,
             self.email,
             self.department,
             self.hire_date
             ]
              )

if __name__  == '__main__':
    employee = Employee()
    print(employee.email)
