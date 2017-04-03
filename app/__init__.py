from flask import Flask
app = Flask(__name__)
app.config.from_object('config')    # 读取配置

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

from app import views
