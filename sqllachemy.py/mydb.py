from sqlalchemy import create_engine,text
from sqlalchemy.orm import declarative_base,sessionmaker
engine=create_engine("mysql+pymysql://root@localhost/")
with engine.connect() as conn:
    conn.execute(text("create database if not exists mydb"))
    
engine=create_engine("mysql+pymysql://root@localhost/mydb")

Base=declarative_base()
session=sessionmaker(bind=engine)
session=session()



