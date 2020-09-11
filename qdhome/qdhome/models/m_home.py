from qdhome.models.meta import Base
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    Float
)


class Home(Base):
    __tablename__ = 'home'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    price = Column(Integer)
    rooms = Column(Integer)
    area = Column(Float)
    m_price = Column(Integer)
    district = Column(Unicode)
    desc_url = Column(Text)