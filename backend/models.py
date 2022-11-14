from database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age='{self.age}')"
