"""
If mysql is available, it will use it. Otherwise it uses the sqlite file
"""
import os


def setupdb(app, db):
    """
    Sets up the database
    """
    if os.getenv("FLASK_ENV") == "test":
        with app.app_context():
            db.drop_all()  # clear and recreate
            db.create_all()

    else:
        with app.app_context():
            db.create_all()
