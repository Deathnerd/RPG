import os, sys, subprocess
from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import MigrateCommand
from rest_rpg.app import create_app, db
from rest_rpg.settings import Production, Development, Staging
from rest_rpg.models import Example

if os.environ.get("REST_RPG_ENV") == "prod":
	app = create_app(Production)
elif os.environ.get("REST_RPG_ENV") == "staging":
	app = create_app(Staging)
else:
	app = create_app(Development)

HERE = os.path.abspath(os.path.dirname(__file__))
# TEST_PATH = os.path.join(HERE, 'tests')

manager = Manager(app)


def _make_context():
	"""
	Return context dict for a shell session so we can access things
	:return:
	"""
	return {'app': app, 'db': db, 'Example': Example}


manager.add_command('server', Server())
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()