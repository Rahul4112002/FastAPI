from pydantic import BaseModel, EmailStr

class EmployeeBase(BaseModel):
    name : str
    email : EmailStr
    
class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass 


class EmployeeOut(EmployeeBase):
    id: int 
    
    class Config:
        orm_mode = True 