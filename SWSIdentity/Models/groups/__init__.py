from sqlalchemy import Column, Integer, String
from SWSIdentity import db


class Groups(db.Model):
    id = Column(Integer, primary_key=True)
    domain = Column(Integer, nullable=False, index=True)
    name = Column(String(128), nullable=False)
    description = Column(String(128))


class RelGroupsUsers(db.Model):
    id = Column(Integer, primary_key=True)
    group = Column(Integer, index=True)
    user = Column(Integer, index=True)
