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


@note.route('/delete_note/<string:id_nos>', methods=['DELETE'])
def delete_note(id_nos):
    del_note = db.get_or_404(Note, id_nos)

    hold = del_note.__dict__
    try:
        db.session.delete(del_note)
        db.session.commit()
    except Exception as e:
        print(str(e))
    return f"The note {hold['title']} has been deleted.", 200
