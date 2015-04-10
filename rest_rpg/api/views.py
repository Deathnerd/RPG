"""Handle all of the api endpoints here"""
from . import *


@api.route("/")
def root():
    return jsonify({'success': True})