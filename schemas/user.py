from pyantic import BaseModel

class User(BaseModel):
    name:str
    email:str
    password:str
