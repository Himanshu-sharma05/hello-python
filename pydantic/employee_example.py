from pydantic import BaseModel,Field
from typing import Optional
import re
class Employee(BaseModel):
    name:str = Field(
        ...,
        min_length=4,
        max_length=20,
        description="Employee name",
        examples="Himanshu Sharma"
    )
    age:int = Field(
        ...,
        ge=18,
        le=120,
        description="Age of the employee",
        examples="18 19 20"
    )
    department:Optional[str] = 'General'


class Voter(BaseModel):
    full_name:str = Field(
        ...,
        min_length=3,
        max_length=25,
        description="Full Name of the voter",
        examples="Himanshu Sharma"
    )
    phone_no:str = Field(...,regex=r'')
    email:str = Field(...,regex=r'')
    age:int = Field(
        ...,
        ge=18,
        le=120,
        description="Age of the voter should be more than 18 "
    )
    adhaar_no:str = Field(...,regex=r'\d\d\d \d\d\d \d\d\d')
    voted:Optional[bool] = False
