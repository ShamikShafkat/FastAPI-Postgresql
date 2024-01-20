from sqlalchemy import Column,ForeignKey,Integer,String,Boolean,Float
from config.database import Base

# this is the structure for a table in database
class Questions(Base):
    # define the table name
    __tablename__ = "questions"
    id = Column(Integer,primary_key=True,index=True)
    question_text = Column(String)
    
class Choices(Base):
    __tablename__ = "choices"
    id = Column(Integer,primary_key=True,index=True)
    choice_text = Column(String,index=True)
    is_correct = Column(Boolean)
    question_id = Column(Integer,ForeignKey("questions.id"))