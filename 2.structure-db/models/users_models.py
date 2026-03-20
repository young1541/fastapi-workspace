from pydantic import BaseModel,EmailStr

from sqlmodel import SQLModel, Field

class User( SQLModel, table=True ):
    id : int = Field( default=None , primary_key=True )
    email : EmailStr = Field(sa_column_kwargs={"unique":True} )
    password : str
    name : str

class UserSingnIn(BaseModel):
    email : EmailStr
    password :str

