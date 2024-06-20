from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app import create_employees

app = FastAPI()
# create a dictionnary containing infos about 20 employees
employees_dict = create_employees(20)
print(employees_dict)


@app.get("/")
def report_employee(employee_id: str) -> JSONResponse:
    if employee_id not in employees_dict.keys():
        return JSONResponse(status_code=404, content="Employee not found")
    else:
        employee_report = employees_dict[employee_id]
        return JSONResponse(status_code=200, content=employee_report)


# curl -v "http://127.0.0.1:8001/?employee_id=626f608a-f2e7-4083-8834-ecf0351c407a"
