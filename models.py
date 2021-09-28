#creating the user table
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
#import datetime as dt
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    First_Name=Column(String)
    Last_Name=Column(String)
    DOB = Column(String)
    #hashed_password = Column(String)
    #is_active = Column(Boolean, default=True)

   #items = relationship("Item", back_populates="owner")