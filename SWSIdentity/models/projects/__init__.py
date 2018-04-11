from sqlalchemy import Column, Integer, String
from SWSIdentity import db


class Projects(db.Model):
    id = Column(Integer, primary_key=True)
    domain = Column(Integer, nullable=False, index=True)
    name = Column(String(128), nullable=False)
    description = Column(String(128))
    enabled = Column(Integer, nullable=False, default=0)
