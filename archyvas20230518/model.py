from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///orders.db')
Base = declarative_base()


class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    f_name = Column(String)
    l_name = Column(String)
    email = Column(String)
    orders = relationship("Order")

    def __repr__(self):
        return f'{self.id} {self.f_name} {self.l_name}'


class Status(Base):
    __tablename__ = "status"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    orders = relationship("Order")

    def __repr__(self):
        return f'{self.id} {self.name}'


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

    def __repr__(self):
        return f'{self.id} {self.name}'


class Order(Base):
    __tablename__ = "order_"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    status_id = Column(Integer, ForeignKey("status.id"))
    customer = relationship("Customer")
    status = relationship("Status")


class OrderProduct(Base):
    __tablename__ = 'order_product'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order_.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer)
    order = relationship("Order")
    product = relationship("Product")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
