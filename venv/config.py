import os

class Config:
    SQLALCHEMY_DATABASEURI = 'sqlite:///' + os.path.join(os.getcwd(), 'test.db')
    SQLALCHEMY_TRACK_MODIFICATION = False