from app import app
from flask import jsonify
from flask import request,render_template

@app.route('/')
def index():
    #return jsonify({'name':'jared','email':'test@qq.com'})
    return render_template("index.html")

@app.route('login')
def login():
    return "can not find login page"
