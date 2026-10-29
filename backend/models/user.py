from sqlalchemy import Column, Integer, String
from database.connection import Base 

class User(Base):

 #__tablename__ is a special attribute used by SQLAlchemy to specify the name of the database table associated with a model.
  
    __tablename__ = "users"



#Column() → SQLAlchemy function used to define a database column.
#constraints → rules for the column, such as requiring a value or preventing duplicates
#DataType → the type of data the column stores.
#we can write variable names in uppercase or lowercase  both

    ID = Column(Integer, primary_key=True, index=True)
    FULL_NAME = Column(String(100), nullable=False)
    HASHED_PASSWORD= Column(String(255), nullable=False)
    EMAIL  = Column(String(255), unique=True, nullable=False)


 