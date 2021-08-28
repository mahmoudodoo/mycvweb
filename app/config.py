import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    POSTS_PER_PAGE = 25
    STATIC_PATH = os.path.join(basedir,'static')
    TEMPLATES_PATH = os.path.join(basedir,'templates')