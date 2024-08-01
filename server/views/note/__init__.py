"""
Creates the notes blueprint
"""
from flask import Blueprint

note = Blueprint('note', __name__)

from server.views.note import create_note


