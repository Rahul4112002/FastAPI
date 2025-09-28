import models, schema, crud
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()


# dependency with the DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# endpoints
# 1. create an employee
@app.post('/employees', response_model=schema.EmployeeOut)
def create_employee(employee: schema.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)


# 2. get all employees
@app.get('/employees', response_model=List[schema.EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)


# 3. get specific employee
@app.get('/employees/{emp_id}', response_model=schema.EmployeeOut)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee Not Found')
    return employee



# 4. update an employee
@app.put('/employees/{emp_id}', response_model=schema.EmployeeOut)
def update_employee(emp_id: int, employee: schema.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db, emp_id, employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail='Employee Not Found')
    return db_employee


# 5. delete an employee
@app.delete('/employees/{emp_id}', response_model=dict)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.delete_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee Not Found')
    # return employee
    return {'detail': 'Employee Deleted'}