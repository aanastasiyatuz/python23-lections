from settings import Base
from sqlalchemy import Column, Integer, String, Text, Numeric


# создаем таблицу продукта
class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(Numeric)
    quantity = Column(Integer)
    description = Column(Text)
