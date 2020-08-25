from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    Float
)

from qdhome.models.meta import Base


class DbMgrUpdate(Base):
    __tablename__ = 'dbmgr_update_settings'
    id = Column(Integer, primary_key=True)
    first_url = Column(Text)
    range_from = Column(Integer)
    range_to = Column(Integer)