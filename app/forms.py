#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""declarate form class"""

from flask_wtf import Form
from wtforms import BooleanField, StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
