from app.data_generator import Employee


def create_employees(number_employees: int) -> dict:
    """
    Creates a dictionnary containing TechCorp company employees informtions
    :return: dictionnary containing informations about fake employees of TechCorp company
    """

    dict_employees = dict()
    for i in range(number_employees):
        employee = Employee()
        dict_employees[employee.id] = employee.generate_employee_report()
    return dict_employees
