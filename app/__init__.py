# 编码设置

from flask import Flask
app = Flask(__name__)
app.config.from_object('config')    # 读取配置

# sql
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# bootstrap
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

# openid login
from flask_openid import OpenID
from flask_login import LoginManager
from config import basedir
import os

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login' # tell LoginManager which view to login
oid = OpenID(app, os.path.join(basedir, 'tmp'))
lm.login_message = None
# views
from app import views, models