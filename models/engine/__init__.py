"""
Ensures that the user has mysql. If they don't it defaults to sqlite file
"""
import os

#check if user is using mysql
DB_TYPE = os.getenv('DB_TYPE', 'sqlite')

basedir = os.path.abspath(os.path.dirname(__file__))
if DB_TYPE == 'sql':
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'SideNotes.sqlite'))
else:
    DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'SideNotes.sqlite')

