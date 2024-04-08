from pydantic import BaseModel
from typing import Optional

#create users
class User(BaseModel):
    email: str
    username: str
    password: str
    
#log in
class Login(BaseModel):
    email: str
    password: str
    
class GetUser(BaseModel):
    email: str
    username: str
    
    class Config:
        orm_mode = True

class UpdateUser(BaseModel):
    username: str
    
    class Config: 
        orm_mode = True
        
class Blogs(BaseModel):
    title: str
    information: str
    
    class Config:
        orm_mode = True
        
#create access token
class Token(BaseModel):
    access_token: str
    token_type: str

#Get Token Data
class TokenData(BaseModel):
    email: Optional[str] | None = None