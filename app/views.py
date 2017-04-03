from app import app
from flask import jsonify
from flask import request

@app.route('/')
def index():
    print(request.__dict__)
    return jsonify({'name':'jared','email':'test@qq.com'})

@app.route('login')
def login():
    return "can not find login page"
