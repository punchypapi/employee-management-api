from app.data_generator import Employee
import unittest
from datetime import date


class TestEmployee(unittest.TestCase):
    def test_email(self):
        employee_test = Employee()
        email = f"{employee_test.first_name.lower()}.{employee_test.last_name.lower()}@techcorp.com"
        self.assertEqual(employee_test.generate_email_adress(), email)

    def test_tenure(self):
        employee_test = Employee()
        tenure = date.today() - employee_test.hire_date
        tenure_year = tenure.days // 365
        self.assertEqual(employee_test.calculate_employee_tenure(), tenure_year)

    def test_senority(self):
        list_tenure_year = [1, 3, 9]
        list_seniority = ["Junior", "Confirmed", "Senior"]
        for i in range(len(list_tenure_year)):
            with self.subTest(i=i):
                employee_test = Employee()
                tenure_year = list_tenure_year[i]
                senority_expected = list_seniority[i]
                self.assertEqual(
                    employee_test.calculate_senority(tenure_year), senority_expected
                )
