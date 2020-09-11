from sqlalchemy import (
    and_,
    or_,
    Column,
    String,
    Integer,
    Float,
    DateTime,
    Unicode,
    ForeignKey,
    UniqueConstraint,
    Boolean,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, event, MetaData
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.inspection import inspect
#from sqlalchemy import DDL

from api.config import URI
engine = create_engine(URI, echo=False)

metadata = MetaData()
Base = declarative_base(metadata=metadata)


gen_session = sessionmaker(bind=engine)
connection = engine.connect()
session = gen_session(bind=connection)

__all__ = [
    "Integer",
    "String",
    "Column",
    "DateTime",
    "Float",
    "inspect",
    "Unicode",
    "ForeignKey",
    "relationship",
    "UniqueConstraint",
    "Boolean",
    "and_",
    "or_"
]
