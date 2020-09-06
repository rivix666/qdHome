from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    Float,
    Boolean
)

from qdhome.models.meta import Base


class AdminSettings(Base):
    __tablename__ = 'dbmgr_update_settings'
    id = Column(Integer, primary_key=True)
    first_url = Column(Text)
    range_from = Column(Integer)
    range_to = Column(Integer)
    info_email = Column(Text)
    should_email = Column(Boolean)
    info_keywords = Column(Text)
