from pydantic import BaseModel,field_validator,model_validator,Field,Optional
import re
class UserData(BaseModel):
    username:str = Field(
        ...,
        min_length=2,
        max_length=25,
        description="name of the user"
    )
    email:str = Field(...,regex=r'')
    password:str 
    confirm_password : str

    @field_validator('username')
    def username_length(cls,v):
        if(len(v) < 3):
            raise ValueError("The username cannot be less than 3")
        return v
    
    @model_validator(mode='after')
    def password_match(cls,values):
        if(values.password != values.confirm_password):
            raise ValueError("Confirm password is different than password.")
        return values

class SignupData(BaseModel):
    username:str
    password:str
    confirm_password:str
    @field_validator('username')
    def check_username(cls,v):
        if(len(v) < 3):
            raise ValueError("username cannot be less than 3")
        return v
    @model_validator(mode='after')
    def check_password(cls,values):
        if(values.password != values.confirm_password):
            raise ValueError("Password is different")
        return values
    
