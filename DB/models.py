from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialization = Column(String)
    number_of_people = Column(Integer)
    tech_support = Column(String)
    tool_support = Column(String)
    objects = relationship("Object", back_populates="supplier")

class Object(Base):
    __tablename__ = 'objects'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    name = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    cost = Column(Float)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    supplier = relationship("Supplier", back_populates="objects")
    orders = relationship("Order", back_populates="object")

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    total_amount = Column(Float)
    information = Column(String)
    object_id = Column(Integer, ForeignKey('objects.id'))
    object = relationship("Object", back_populates="orders")