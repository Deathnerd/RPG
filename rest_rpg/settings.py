__author__ = 'Deathnerd'
import os


class Base():
	"""Base Config"""
	SECRET_KEY = "S00pp3rS3cr3t"
	APP_DIR = os.path.abspath(os.path.dirname(__file__))
	PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
	SQLALCHEMY_DATABASE_URI = "sqlite:///dbase.db"
	BCRYPT_LOG_ROUNDS = 13
	DEBUG_TB_ENABLED = False
	DEBUG_TB_INTERCEPT_REDIRECTS = False


class Production(Base):
	"""Production Config"""
	ENV = 'prod'
	DEBUG = False
	DEBUG_TB_ENABLED = False


class Development(Base):
	"""Development Config"""
	ENV = "dev"
	DEBUG = True
	DEBUG_TB_ENABLED = True


class Staging(Base):
	"""Staging Config"""
	TESTING = True
	DEBUG = True
	BCRYPT_LOG_ROUNDS = 1
	WTF_CSRF_ENABLED = False