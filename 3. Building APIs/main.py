from fastapi import FastAPI , HTTPException
from models import Employee
from typing import List

employees_db: List[Employee] = []

app = FastAPI()

# 1. Read all the Employees
@app.get('/employees', response_model=List[Employee])
def get_employees():
    return employees_db


# 2. Read Specific employees
@app.get('/employees/{emp_id}', response_model=Employee)
def get_employee(emp_id: int):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            return employees_db[index]
    raise HTTPException(status_code=404, detail='Employee Not Found')
    
# 3. Add an employee
@app.post('/add_employee', response_model=Employee)
def add_employee(new_emp: Employee):
    for employee in employees_db:
        if employee.id == new_emp.id:
            raise HTTPException(status_code=400, detail="Employee Already Exists")
    employees_db.append(new_emp)
    return new_emp

#4. Update an Employee
@app.put('/update_employee/{emp_id}', response_model=Employee)
def update_employee(emp_id: int, updated_employee: Employee):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            employees_db[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee Not Found")

# 5. Delete an Employee
@app.delete('/delete_employee/{emp_id}', response_model=Employee)
def delete_employee(emp_id:int):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            del employees_db[index]
            return {'message': "Employee Deleted Successfully"}
    raise HTTPException(status_code=404, detail='Employee not found')
    
                
        