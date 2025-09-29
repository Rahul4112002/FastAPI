from pydantic import BaseModel, StrictInt, Field

class InputSchema(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: int = Field(..., gt=0)
    total_rooms: StrictInt = Field(...,gt=0)
    total_bedrooms: StrictInt = Field(...,gt=0)
    population: StrictInt = Field(...,gt=0)
    households: StrictInt = Field(...,gt=0)
    median_income: float = Field(...,gt=0)
    
class OutputSchema(BaseModel):
    predicted_price: float
    
    

