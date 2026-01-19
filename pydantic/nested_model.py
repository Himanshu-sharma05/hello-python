from pydantic import BaseModel,Field
from typing import Optional
import re
class Address(BaseModel):
    street:str
    city:str
    pincode:int
    country:str

class User(BaseModel):
    name:str
    email:str 
    phone: str = Field(
        ...,
        pattern=r"^[6-9]\d{9}$"
        )
    address:Address | None = None

address = {"street":"56","city":"delhi","pincode":"06","country":"india"}
user = {
    "name":"Himanshu",
    "email":"himanshu@gmail.com",
    "phone":"8450000000",
    "address":address
}

user_object = User(**user)

print(user_object)