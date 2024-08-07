"""
Creates the notes blueprint
"""
from flask import Blueprint

note = Blueprint('note', __name__)

from server.views.note.create_note import create_note
from server.views.note.view_note import view_notes


