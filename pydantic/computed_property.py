from pydantic import BaseModel,computed_field,Field
from typing import List

class Product(BaseModel):
    id:int
    name:str
    price:float
    quantity:int

    @computed_field
    @property
    def totalPrice(self)->float:
        return self.price * self.quantity
    

class Booking(BaseModel):
    userId:int
    userName:str
    price_perNight:float
    booking_nights:int = Field(...,ge=1)
    @computed_field
    @property
    def total_amount(self)->float:
        return self.price_perNight*self.booking_nights
    
user_data = {
    "userId":32984723,
    "userName":"DexterMorgan67",
    "price_perNight":1500.00,
    "booking_nights":5,
}

validated_user = Booking(**user_data)
print(validated_user.total_amount)





    
    
    
