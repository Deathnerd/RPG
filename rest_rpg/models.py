from .app import db


class Example(db.Model):
    __name__ = "Example"
    session = db.session
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    value = db.Column(db.String(100), nullable=False)

    def __init__(self, **kwargs):
        for key, value in kwargs:
            setattr(self, key, value)

    def __repr__(self):
        return "{name}:{value}".format(name=self.name, value=self.value)