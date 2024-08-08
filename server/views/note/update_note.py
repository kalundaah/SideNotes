"""
Delete note
"""
# dependencies
from flask import request
# blueprint
from . import note
# db
from server import db
# Notes model
from models.note import Note


@note.route('/update_note/<string:id_nos>', methods=['PUT'])
def update_note(id_nos):
    upd_note = db.get_or_404(Note, id_nos)
    data = request.get_json()
    if data is None:
        return f"Nothing to update", 200
    else:
        upd_note.title = data['title']
        upd_note.content = data['content']
    try:
        db.session.commit()
    except Exception as e:
        print(str(e))
    return f"The note {upd_note.title} has been modified.", 200
