from database import Base
from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    blogs = relationship("Blog", back_populates="owner")


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)


    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="blogs") # class ir