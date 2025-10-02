from sqlalchemy import Column,Integer,String
from mydb import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer,nullable=False,autoincrement=True,primary_key=True)
    name=Column(String(100),nullable=False)
    age=Column(Integer)
    
