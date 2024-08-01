"""
This is for general URLs that contain navigation etc.
"""
from flask import Blueprint

general = Blueprint('general', __name__)

from server.views.general import home




