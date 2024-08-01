"""
The note model. Contains a title,content for now.
"""
from server import db


class Note(db.Model):
    """
    A note model. Contains a title,content for now.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=True)



