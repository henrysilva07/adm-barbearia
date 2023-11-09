from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("conf.config")

db = SQLAlchemy(app)

# instanciando view home
from app.views.home import *