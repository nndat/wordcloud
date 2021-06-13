from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime


Base = declarative_base()


class WordCloud(Base):
    __tablename__ = 'wordcloud'
    id = Column(Integer, primary_key=True)
    file_path = Column(String)
    label = Column(String)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.now())
