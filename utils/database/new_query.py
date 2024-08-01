"""
This holds a function that adds a new query to the database.
"""

from server import db


def commit(db,row):
    """
    takes a db session and a row and adds a new query to the database.
    """
    try:
        db.session.add(row)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return str(e)

