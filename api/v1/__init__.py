"""__init__.py """

from flask import Flask

app = Flask(__name__)

app.config.from_pyfile('../../config.py')

from api.v1 import views