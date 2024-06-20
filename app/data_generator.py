import numpy as np
import uuid
from datetime import date, timedelta


def random_first_name():
    """
    open first-names.txt file and returns a first name
    :return: first name
    """
    # Ensure reproducibility of measurements
    with open(
        "/Users/Oussama/employee-management-api/fake_data/first-names.txt", "r"
    ) as f:
        names = f.readlines()
        first_name = np.random.choice(names).strip()
    return first_name


def random_last_name() -> str:
    """
    open last-names.txt file and returns a last name
    :return: last name
    """

    with open(
        "/Users/Oussama/employee-management-api/fake_data/last-names.txt", "r"
    ) as f:
        names = f.readlines()
        last_name = np.random.choice(names).strip()
    return last_name


def random_date() -> date:
    """
    generate a random date
    :return: date
    """
    year = np.random.randint(1980, 2024)
    month = np.random.randint(1, 13)
    day = np.random.randint(1, 28)
    return date(year, month, day)


list_department = ["HR", "IT", "SALE", "MARKETING"]
list_seniority = ["Junior", "Confirmed", "Senior"]


class Employee:
    """
    Simulate an employee in TechCorp company
    Take an id, first name, last name, department, and hire date
    and create an object Employee
    """

    def __init__(self) -> None:
        self.id = uuid.uuid4()
        self.first_name = random_first_name()
        self.last_name = random_last_name()
        self.full_name = f"{self.first_name} {self.last_name}"
        self.department = np.random.choice(list_department)
        self.hire_date = random_date()

    def generate_email_adress(self) -> str:
        """
        Methods that returns email adress of specific employee using his first and last name
        :return: email adress of employee
        """
        email = f"{self.first_name.lower()}.{self.last_name.lower()}@techcorp.com"
        return email

    def calculate_employee_tenure(self) -> int:
        """
        method to calculate the number of years an employee has been with the company based on their hire date.
        :return: Number of years employee has been in the compagny
        """
        tenure = date.today() - self.hire_date
        return tenure.days // 365

    def calculate_senority(self, tenure_year: int) -> str:
        """
        Method to compute a senority of employee
        :return: senority of a specific employee
        """
        if tenure_year > 4:
            return list_seniority[2]
        else:
            if tenure_year < 2:
                return list_seniority[0]
            if tenure_year > 2:
                return list_seniority[1]

    def generate_employee_report(self) -> dict:
        """
        :return: dictionnary containing a report about a specific employee
        """
        report = {
            "id": self.id,
            "full name": self.full_name,
            "email adress": self.generate_email_adress(),
            "department": self.department,
            "hire date": self.hire_date,
            "tenure (years)": self.calculate_employee_tenure(),
            "seniority": self.calculate_senority(self.calculate_employee_tenure()),
        }
        return report

    def promote_employee(self) -> None:
        """
        Methods that promote employees with > 10 years of tenure
        :return: None
        """


if __name__ == "__main__":
    employee = Employee()
    print(employee.generate_employee_report())
