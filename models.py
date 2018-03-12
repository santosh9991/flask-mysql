from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://<user_name>:<pw>@127.0.0.1:3306/localdb', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()
class CPUModel(Base):
    __tablename__ = 'cpu'
    cpu_id = Column(Integer,primary_key=True)
    cpu_name = Column(String(50),nullable=False)
    location = Column(String(50),ForeignKey('locations.location_id'))
    # customer_id = Column(Integer, ForeignKey('demo_customers.customer_id'))
    locs = relationship('LocationModel',backref='locations',lazy=True)
class LocationModel(Base):
    __tablename__ = 'locations'
    location_id = Column(String(50),primary_key=True)
    city = Column(String(50),nullable=False)
    state = Column(String(50))
