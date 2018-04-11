from sqlalchemy import Column, Integer, String
from SWSIdentity import db


class Domains(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    description = Column(String(128))
    enabled = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return "<Domain id={} name={} enabled={}>".format(
            self.id, self.name, self.enabled
        )
