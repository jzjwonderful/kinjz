#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""declarate form class"""

from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class LoginUsr(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class UserInfo():
    nickname = ""
    email = ""
    def  __init__(self,nickname,email):
        self.nickname = nickname
        self.email = email

    def __repr__(self):
        return '<nickname %r, email %r>' % (self.nickname,self.email)