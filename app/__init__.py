from flask import Flask
app = Flask(__name__)
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

from app import views
