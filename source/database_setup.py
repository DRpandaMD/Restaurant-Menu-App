# database_setup.py
# a database setup python file to create and setup a database

# imports
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


# Lets make the Base class
Base = declarative_base()

# Now we are going to make two separate classes that represent the two separate tables in the DB
class Restaurant(Base):
    __tablename__ = 'restaurant'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)


class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    restaurant = relationship(Restaurant)

    # This Block will be used to serialize data for our JSON Objects that will be added
    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'course': self.course,
            'description': self.description,
            'price': self.price
        }


# this part will always get inserted at EOF #
engine = create_engine('sqlite:///restaurant_menu.db')
Base.metadata.create_all(engine)
