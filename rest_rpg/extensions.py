# -*- coding: utf-8 -*-
"""
All of our extensions are initialized here. They are registered in
app.py:register_extensions upon app creation
"""
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask.ext.migrate import Migrate
migrate = Migrate()

from flask.ext.debugtoolbar import DebugToolbarExtension
debug_toolbar = DebugToolbarExtension()

from flask.ext.bcrypt import Bcrypt
bcrypt = Bcrypt()

from flask.ext.superadmin import Admin
admin = Admin(name="Rest Player Generator (RPG)")