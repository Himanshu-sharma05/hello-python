from pydantic import BaseModel,field_validator,model_validator
from datetime import datetime
from typing import List

class Product(BaseModel):
    id:int
    name: str
    price: float
    @field_validator('name',mode = 'before')
    def normalizeName(cls,v):
        return v.lower().strip()


class User(BaseModel):
    name: str
    phone: int
    cart: List[Product] = []


class Timing(BaseModel):
    start_time:datetime
    end_time:datetime

    @model_validator(mode="after")
    def validate_date_time(cls,values):
        if values.start_time > values.end_time:
            raise ValueError("Start time cannot be larger than end time ")
        return values


    


    