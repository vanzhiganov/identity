from SWSIdentity import db


class Domains(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128))
    enabled = db.Column(db.Integer, default=0)
