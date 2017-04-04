#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" import module or package"""
from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    """ setup index route """
    #return jsonify({'name':'jared','email':'test@qq.com'})
    return render_template("index.html")


@app.route('/login', methods = ['GET', 'POST'])
def login():
    """ setup login route """
    form = LoginForm()
    if form.validate_on_submit():
        flash('login success with:' + form.openid.data + 'rember me with:'+str(form.remember_me.data))
        return redirect('/index')
    return render_template("login.html",title="Login",form=form,
    providers = app.config['OPENID_PROVIDERS'])
