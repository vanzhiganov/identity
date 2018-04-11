from sqlalchemy import Column, Integer, String
from SWSIdentity import db


class Users(db.Model):
    id = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False)
    password = Column(String(32))
    enabled = Column(Integer, nullable=False, default=0)


class RelUsersRoles(db.Model):
    id = Column(Integer, primary_key=True)
    user = Column(Integer, index=True)
    role = Column(Integer, index=True)
