from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    is_available:bool = True
    price:int

product1 = Product(id=1,name='laptop',is_available=False,price=50)
product2 = Product(id=2,name='mouse',price=60)
print(product2)


