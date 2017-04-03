from app import app
from flask import jsonify
from flask import request,render_template

@app.route('/')
@app.route('/index')
def index():
    #return jsonify({'name':'jared','email':'test@qq.com'})
    return render_template("index.html")

@app.route('/login')
def login():
    return "cann't find login page"
