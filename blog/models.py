from sqlalchemy import Column, Integer, String
from .database import Base  # Import Base from database.py

# Define the Blog model (table)
class Blog(Base):
    __tablename__ = "blogs"  # Table name in the database

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # Primary Key
    title = Column(String, index=True)  # Title column
    body = Column(String)  # Body column
