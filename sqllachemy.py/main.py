from crud import create_user,get_user,get_by_id,update,delete
from mydb import Base,engine
import models
Base.metadata.create_all(bind=engine)
while True:
    print("---------- Welcome!-------")
    print("1: Add user")
    print("2: Check all")
    print("3: check by id")
    print("4: Update by id")
    print("5: Delete by id")
    print("6: Exit")
    try:
        n=int(input("Enter your choice ").strip())
        if n==1:
            #  ╔════════════════════╗
            #  ║     Add user       ║
            #  ╚════════════════════╝
            name=input("Enter your name ").capitalize().strip()
            age=int(input("Enter your age ").strip())
            user=create_user(name,age)
        elif n==2:
            #  ╔════════════════════╗
            #  ║     Check all      ║
            #  ╚════════════════════╝
            users=get_user()
            if users:
              for i in users:
                print(f"{i.id} {i.name} {i.age}")
        elif n==3:
            #  ╔════════════════════╗
            #  ║     Check by id    ║
            #  ╚════════════════════╝
            id=int(input("enter "))
            user=get_by_id(id)
        elif n==4:
            #  ╔════════════════════╗
            #  ║     Update by id   ║
            #  ╚════════════════════╝
            id=int(input("Enter your id "))
            new_name=input("Enter your name  ")or None
            new_age=input("Enter your age ") or None
            user=update(id,new_name,new_age)
            print(f"{user.id} {user.name} {user.age}")
        elif n==5:
            #  ╔════════════════════╗
            #  ║     Delete by id   ║
            #  ╚════════════════════╝
            id=int(input("Enter your id  "))
            user=delete(id)
        elif n==6:
            break
    except:
        print("Plz enter value in integers")
            
            
            

    

        
