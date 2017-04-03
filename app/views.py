#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" import module or package"""
from app import app
from flask import render_template
from flask_bootstrap import Bootstrap
@app.route('/')
@app.route('/index')
def index():
    """ setup index route """
    #return jsonify({'name':'jared','email':'test@qq.com'})
    return render_template("index.html")


@app.route('/login')
def login():
    """ setup login route """
    return "cann't find login page"
