from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

from sqlalchemy_i18n import make_translatable, Translatable
make_translatable(options={
    'locales': ['en', 'fr'],
    'get_locale_fallback': True
})

class MyModel(Base, Translatable):
    __tablename__ = 'models'
    __translated_columns__ = [
        Column('description', Text)
    ]
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_locale(self):
        pass

Index('my_index', MyModel.name, unique=True, mysql_length=255)
