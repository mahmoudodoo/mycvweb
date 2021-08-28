from flask import Flask
from app.config import Config
from flask import render_template,redirect,request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)


from app.views import about_me_view