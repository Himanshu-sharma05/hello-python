from pydantic import BaseModel
from typing import List,Dict,Optional

class Cart(BaseModel):
    user_id:int
    product:List[str]
    product_quantity:Dict[str,int]

class BlogPost(BaseModel):
    title:str
    content:str
    image:Optional[str] = None

class User(BaseModel):
    name:str
    phone_no:int
    user_id:str
    interests:List[str]
    gender:Optional[str]
    

