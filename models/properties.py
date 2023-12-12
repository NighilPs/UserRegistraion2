from sqlalchemy import Boolean, Column, ForeignKey, Integer, String    
from storage.database import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String )
    email = Column(String, unique=True)
    password = Column(String)
    phone = Column(String)

class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    image = Column(String)
    filename = Column(String)
    content_type = Column(String)