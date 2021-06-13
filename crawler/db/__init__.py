from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base, WordCloud


def get_engine():
    engine = create_engine('sqlite:///test.db')
    return engine


def get_session():
    engine = get_engine()
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


def init_db():
    engine = get_engine()
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)


def test():
    wc = WordCloud(file_path="test.png", content="test", label="test")
    session = get_session()
    session.add(wc)
    session.commit()


if __name__ == "__main__":
    test()
