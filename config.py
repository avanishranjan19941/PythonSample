import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:admin@localhost/connector')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
