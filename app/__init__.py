#__init__.py

from flask import Flask

app = Flask(__name__)

app.config.from_pyfile('../config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #silence deprecation warnings

from app import views