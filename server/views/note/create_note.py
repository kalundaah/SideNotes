"""
Create note
"""
# dependencies
from flask import request
# blueprint
from . import note
# db
from server import db
# Notes model
from models.note import Note


@note.route('/create', methods=['POST'])
def create_note():
    """
    A note must contain at least a heading for it to be created
    """
    data = request.get_json()
    required_fields = ['title']  # Title must be there for a note to be created.
    title = data['title']
    if not title:
        return "Title cannot be empty", 400  # If title is not there it cannot be empty
    else:
        content = data.get('content', None)  # Check if content is available
        if content is None:
            new_note = Note(title=title)
            from utils.database.new_query import commit
            e = commit(db=db,
                       row=new_note)
            if e is None:
                return f"The note '{title}' has been made successfully", 200
            else:
                print(e)
                return f"The note '{title}' has not been created", 400
        else:
            new_note = Note(title=title, content=content)
            from utils.database.new_query import commit
            e = commit(db=db,
                       row=new_note)
            if e is None:
                return f"The note '{title}' with '{content}' has been made successfully", 200
            else:
                print(e)
                return f"The note '{title}' has not been created", 400
