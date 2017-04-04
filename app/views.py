#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" import module or package"""
from flask_login import login_user, logout_user, current_user, login_required
from app import app, lm, oid, db
from flask import render_template, flash, redirect, session, url_for, request, g
from .forms import LoginForm, LoginUsr
from .models import User

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/index')
@login_required # only show if user login
def index():
    """ setup index route """
    print('called index()')
    user = g.user
    posts = [
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",user = user, post=posts)


@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
    """ setup login route """
    print('called login1()')
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    print('called login2()')
    #form = LoginForm()
    form = LoginUsr()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        print(form.nickname.data,form.email.data)
        #return oid.try_login(form.openid.data, ask_for=['nickname', 'email']) # asyn call,if success,call after_login
        resp.nickname = form.nickname
        resp.email = form.email
        return after_login(resp)
    print('called login3()')
    return render_template("login.html",title="Login",form=form,
    providers = app.config['OPENID_PROVIDERS'])


@oid.after_login
def after_login(resp):
    print('called after_login()')
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@lm.user_loader
def load_user(id):
    print('called load_user()')
    return User.query.get(int(id))

@app.route('/logout')
def logout():
    print('called logout()')
    logout_user()
    return redirect(url_for('index'))
