from SWSIdentity import db


class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.Integer, nullable=False, index=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128))


class RelGroupsUsers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.Integer, index=True)
    user = db.Column(db.Integer, index=True)
