#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" import module or package"""
from flask_login import login_user, logout_user, current_user, login_required
from app import app, lm, oid, db
from flask import render_template, flash, redirect, session, url_for, request, g
from .forms import LoginForm, LoginUsr, UserInfo
from .models import User
import datetime, time

def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    # value为传入的值为时间戳(整形)，如：1332888820
    value = time.localtime(value)
    ## 经过localtime转换后变成
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    # 最后再经过strftime函数转换为正常日期格式。
    dt = time.strftime(format, value)
    return dt

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
        resp = UserInfo(form.nickname.data,form.email.data)
        #return oid.try_login(form.openid.data, ask_for=['nickname', 'email']) # asyn call,if success,call after_login
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

    # get utc timestamp int value
    timestamp = datetime.datetime.utcnow()
    datetime.datetime.ti
    timestamp.
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email,regtime = timestamp)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    current_time =  timestamp.astimezone(timezone(timedelta(hours=8)))
    print('%r,%r' %timestamp,)
    flash('welcome to www.kin.xyz, current time: %s' % timestamp)
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
