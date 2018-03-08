
from SWSIdentity import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(32))
    enabled = db.Column(db.Integer, nullable=False, default=0)
