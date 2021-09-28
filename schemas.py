#It will shape the model/data that our api receives and respond with (layout)
from pydantic import BaseModel , Field 

class UserBase(BaseModel):
    First_Name:str
    Last_Name:str
    DOB:str


class User(UserBase):
    id:int
    class Config():
        orm_mode=True

class del_user(BaseModel):
    id:int = Field(...,type=int)
    #class Config():
     #   orm_mode=True
    