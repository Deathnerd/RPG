from .app import db


class Example(db.Model):
	__name__ = "Example"
	session = db.session
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True)
	value = db.Column(db.String(100), nullable=False)

	def __init__(self, key, value, *args, **kwargs):
		self.key = key
		self.value = value

	def __repr__(self):
		return "<Example {name}:{value}>".format(name=self.name, value=self.value)