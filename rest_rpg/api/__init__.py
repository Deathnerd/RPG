__author__ = 'deathnerd'
from flask import Blueprint, request, render_template, url_for, redirect, session, jsonify
from rest_rpg.app import db


api = Blueprint('api', __name__, static_folder="../static")

from . import views
from . import models