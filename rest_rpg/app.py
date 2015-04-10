from flask import Flask
from .settings import Production
from flask.ext.superadmin import model
from .extensions import bcrypt, db, migrate, debug_toolbar, admin
from .models import Example


def create_app(config_object=Production):
	"""
	Application factory following the pattern at:
	http://flask.pocoo.org/docs/patterns/appfactories/

	:param config_object: The configuration object that we'll be using
	:returns app:
	"""
	app = Flask(__name__)
	app.config.from_object(config_object)
	register_extensions(app)
	register_admin(Example, session=db.session)

	# admin requires a custom setup
	admin_views()
	return app


def register_extensions(app):
	"""
	Given an app object, initialize the application extensions
	:param app: The current application
	:returns None:
	"""
	bcrypt.init_app(app)
	db.init_app(app)
	migrate.init_app(app, db)
	debug_toolbar.init_app(app)
	admin.init_app(app)
	return None


def register_admin(*args, **kwargs):
	"""
	Takes in any number of unnamed args assuming they're database model classes
	and registers them with the SuperAdmin
	:returns None:
	"""
	for model in args:
		admin.register(model, session=kwargs['session'])
	return None


def admin_views():
	from .admin import views
	admin.add_view(views.MyView(name="Hello 1", endpoint="test1", category="Test"))
	admin.add_view(views.MyView(name="Hello 2", endpoint="test2", category="Test"))
	admin.add_view(views.MyView(name="Hello 3", endpoint="test3", category="Test"))
	return None