from sqlalchemy import Column, Integer, String
from SWSIdentity import db


class Users(db.Model):
    id = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False)
    password = Column(String(512))
    salt = Column(String(36))
    enabled = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return "<user id={} email={}>".format(self.id, self.email)


class RelUsersRoles(db.Model):
    id = Column(Integer, primary_key=True)
    user = Column(Integer, index=True)
    role = Column(Integer, index=True)
