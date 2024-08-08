"""
The note model. Contains a title,content for now.
"""
from datetime import datetime

from server import db
import uuid


class Note(db.Model):
    """
    A note model. Contains a title,content for now.
    """
    id = db.Column(db.String(36), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=True)

    def __init__(self, title, content=None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.content = content
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at