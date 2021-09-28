#Setting up the sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SqlAlchemy_Database_URL= "sqlite:///./data.db"

#by default sql lite only allow one thread to communicate but python function send multiple threads to communicate
engine = create_engine(SqlAlchemy_Database_URL,connect_args={"check_same_thread": False})

session_local=sessionmaker(autocommit=False, autoflush=False, bind=engine)

#use when we create our users and post model we will be overriding or inheriting from Base
Base=declarative_base()

#hii
#fkcmk