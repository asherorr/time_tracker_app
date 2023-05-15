from sqlalchemy import (create_engine, Column, Integer, String, Date)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///time_tracker.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Tracker(Base):
    __tablename__ = "Time_Spent_And_Stats"
    id= Column(Integer, primary_key=True)
    #day = Column("Day", Date)
    time_spent = Column("Time Spent (Minutes)", Integer)
    
def __repr__(self):
    return f'Day: {self.day} Time Spent: {self.time_spent}'