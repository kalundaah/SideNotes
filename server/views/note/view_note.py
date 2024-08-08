"""
Create note
"""
# dependencies
from flask import request, jsonify
# blueprint
from . import note
# db
from server import db
# Notes model
from models.note import Note


@note.route('/view_notes', methods=['GET'])
def view_notes():
    """
    Grabs all the notes.
    """
    notes = Note.query.order_by(Note.id.desc()).all()
    if notes is not None:
        all_notes = []
        for notes_row in notes:
            dict = notes_row.__dict__  # for each class obtain a list of values defined in the class
            dict.pop('_sa_instance_state')
            all_notes.append(dict)            # append the dictionary
        return jsonify({"Notes": f"{all_notes}"}), 200
    else:
        print("Not found")
        return jsonify({"Empty": "No notes found"}), 404


@note.route('/view_note/<id_nos>', methods=['POST'])
def view_note(id_nos):
    note = db.get_or_404(Note, id_nos)
    if note is None:
        return jsonify({"Empty": "No note found"}), 404
    else:
        dict = note.__dict__  # for each class obtain a list of values defined in the class
        dict.pop('_sa_instance_state')
        return jsonify({"Notes": f"{dict}"}), 200
