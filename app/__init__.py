from flask import Flask
app = Flask(__name__)
app.config.from_object('config')    # 读取配置

# sql
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# bootstrap
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

# views
from app import views, models

# openid 
from flask_openid import OpenID

# login
from flask_login import LoginManager

