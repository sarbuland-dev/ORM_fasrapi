from mydb import session
from models import User

#  ╔════════════════════╗
#  ║     create user    ║
#  ╚════════════════════╝
def create_user(name:str,age:int):
    new_user=User(name=name,age=age)
    session.add(new_user)
    session.commit()

#  ╔════════════════════╗
#  ║     Read all       ║
#  ╚════════════════════╝
def get_user():
    
    try:
        return session.query(User).all()
    finally:
        session.close()
        
#  ╔════════════════════╗
#  ║     Read by id     ║
#  ╚════════════════════╝
def get_by_id(id:int):
    try:
        user= session.query(User).filter(User.id==id).first()
        if user:
            print(f"{user.id} {user.name} {user.age}")
    finally:
        session.close()

#  ╔════════════════════╗
#  ║     Update         ║
#  ╚════════════════════╝
            
def update(id:int,new_name:str=None,new_age:int=None):
    try:
        user=session.query(User).filter(User.id==id).first()
        if user:
            if new_name:
                user.name=new_name
            
            if new_age:
                user.age=new_age
            session.commit()
            session.refresh(user)
        return user
    finally:
        session.close()

#  ╔════════════════════╗
#  ║     Delete         ║
#  ╚════════════════════╝

def delete(id:int):
    try:
        user=session.query(User).filter(User.id==id).first()
        session.delete(user)
        session.commit()
    finally:
        session.close()
        

        