from database import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

#For creating users

class User(Base):
    
    __tablename__ = "User"
    
    id = Column(Integer, index = True, primary_key = True)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    datetime = Column(DateTime, default=datetime.utcnow)
    
    blogs = relationship("Blogs", back_populates= 'user')
    
class Blogs(Base):
    
    __tablename__ = "Blogs"
    
    id = Column(Integer, primary_key=True, index= True)
    title = Column(String)
    information = Column(String)
    userEmail = Column(String, ForeignKey('User.email', ondelete="SET NULL"), nullable=True)
    datetime = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates= 'blogs')
    
    