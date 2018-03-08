from SWSIdentity import db


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.Integer, nullable=False, index=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128))
    enabled = db.Column(db.Integer, nullable=False, default=0)
